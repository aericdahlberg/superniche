import psycopg2
from fpdf import FPDF
from datetime import datetime
import io
from PIL import Image
from pdf_class import PDFclass 


# Connect to PostgreSQL

pdf_instance = PDFclass()

# Fetch Data

class Agenda():  
    def get_agenda_data(cursor):
        query = "SELECT * FROM agenda order by session_track"  
        cursor.execute(query)
        return cursor.fetchall()
    
    
    def get_speakers(in_session_id,cursor):
        query = "select * from speakers where session_id = " + str(in_session_id)
        cursor.execute(query)
        return cursor.fetchall()
    
    def speaker_processing(speaker_info):
        #print(str(speaker_info) + ' and of the type... ' , type(speaker_info))
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
    def speakers_to_pdf(pdf, speaker_processed):
        for i in range(0, len(speaker_processed), 3):
            name = speaker_processed[i]
            title = speaker_processed[i+ 1]
            company = speaker_processed[i +2]     
            PDFclass.add_speaker_list(pdf, name, title, company)

#