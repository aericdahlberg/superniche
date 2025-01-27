import psycopg2
from fpdf import FPDF
from agenda_test import Agenda
from pdf_class import PDFclass
from event import Event
from doc_class import WordDocument


conn = psycopg2.connect(
    dbname="poc", user="postgres", password="xFl201X20FabSN2024Nov", host="localhost", port="5432"
)
cursor = conn.cursor()



# Fetch event data
event_data = Event.get_event_data(cursor)
#print ('\n' + 'EVENT DATA ' + '\n')
#print (event_data)

# Fetch agenda Data
agenda_data = Agenda.get_agenda_data(cursor)
# print ('\n' + 'AGENDA DATA ' + '\n')
# print (agenda_data)

# Create PDF
pdf = FPDF()
pdf.add_page()

# Create Word Document
wordDoc = WordDocument ('word_agenda.docx')

##Add Event Data to PDF
for row in event_data:
    event_id, title, image_data, description, content, event_date  = row
   # check types of returns
    #print(type(event_id),event_id, '\n',type(title), title, '\n', type(image_data), image_data, '\n', type(description), description, '\n', type(event_date), event_date, '\n', type(content), content, '\n')
    
    # Add Event information
    PDFclass.header(pdf, title)
    # Add Image if Present
    PDFclass.add_image(pdf, image_data)
    PDFclass.add_event_details(pdf, event_date.strftime('%d %B, %Y'), description)
    PDFclass.add_section(pdf, content)
    
    
    ##doc generation
    wordDoc.create_heading(title, 1)
    wordDoc.add_image2(image_data)
    wordDoc.create_total_heading(title, image_data)
    wordDoc.add_event_details(event_date.strftime('%d %B, %Y'), description)
    wordDoc.add_session(title, event_date.strftime('%H:%M'), content)

#now add agenda data in within each agenda point, speaker data
for row in agenda_data:
    session_id, session_time, title, abstract, session_track = row
    #check types of returns
        #print(type(session_id),session_id, '\n',type(session_time), session_time, '\n', type(title), title, '\n', type(abstract), abstract, '\n', type(session_track), session_track, '\n')
                
                
                ## **  ** ##
                #format this later... do i need to use datetime strip function to make it pop)
                ## **  ** ##
    PDFclass.add_agenda_item(pdf, title, str(session_time), abstract)
       
    wordDoc.add_session(title, str(session_time), abstract)
                    
                    
                    
                    
    speaker_info = Agenda.get_speakers(session_id, cursor)
    speaker_processed = Agenda.speaker_processing(speaker_info)
    print (speaker_processed)
    Agenda.speakers_to_pdf(pdf,speaker_processed)
    wordDoc.speakers_to_doc(speaker_processed)
    
        
        

    # Save PDF
pdf.output("web3_event_test.pdf")

    # Save Word Document
wordDoc.save()
cursor.close()
conn.close()

