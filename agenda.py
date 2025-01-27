import psycopg2
from fpdf import FPDF
from datetime import datetime
import io
from PIL import Image
from pdf_class import PDFclass
## eventually use from supernicheX import def_name to clean this up... 



# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="poc", user="postgres", password="xFl201X20FabSN2024Nov", host="localhost", port="5432"
)
cursor = conn.cursor()
pdf_instance = PDFclass()

# Fetch Data
query = "SELECT * FROM agenda order by session_track"  
cursor.execute(query)
rows = cursor.fetchall()
            
# Create PDF
pdf = PDF()
pdf.add_page()

def get_speakers(in_session_id):
    query = "select speakers.* from speakers left join agenda on speakers.session_id = " + str(in_session_id)
    cursor.execute(query)
    speaker_info = cursor.fetchall()
    print(str(speaker_info) + ' and of the type... ' , type(speaker_info))
    if len(speaker_info) == 0:
        return ["add speaker name", "add speaker title", "add speaker company"]
    else:
        speakerinfo=[]
        for speaker_row in speaker_info:
            speaker_id, first_name, last_name, job_title, company_name, company_type, speaker_thumbnail, email, session_id = speaker_row
            speakerinfo.append(first_name + " " + last_name)
            speakerinfo.append(job_title)
            speakerinfo.append(company_name) 
            ### check if null values mess up the above arrays 
        return speakerinfo
def speakers_to_pdf(speaker_info):
     for i in range(0, len(speaker_info), 3):
        name = speaker_info[i]
        title = speaker_info[i+ 1]
        company = speaker_info[i +2]     
        pdf.add_speaker_list(name, title, company)

print (rows, '\n')
for row in rows:
    session_id, session_time, title, abstract, session_track = row
   
    
   # check types of returns
    print(row) , '\n'
    print(type(session_id),session_id, '\n',type(session_time), session_time, '\n', type(title), title, '\n', type(abstract), abstract, '\n', type(session_track), session_track, '\n')
   
   
    my_instance.add_session(title, str(session_time), abstract)
                                            #format this later... do i need to use datetime strip function to make it pop)
    
    
    speaker_info = get_speakers(session_id)
    speakers_to_pdf(speaker_info)
        
        
    
    
    

# Save PDF
pdf.output("web3_event_agenda1.pdf")

# Close Database Connection
cursor.close()
conn.close()