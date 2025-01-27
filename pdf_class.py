import psycopg2
from fpdf import FPDF
from datetime import datetime
import io
from PIL import Image

class PDFclass(FPDF):  
    
       #  Event functions #
    def header(pdf, title):
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, title, align = 'C', ln=1)
        pdf.ln(5)
        
    def add_image(pdf, image_data):
        if image_data:
            image = Image.open(io.BytesIO(image_data))
            if image.mode != "RGB":
                image = image.convert("RGB")
            image.save("temp_image.jpg")  # Save the image temporarily
            pdf.image("temp_image.jpg", x=10, y=pdf.get_y(), w=100)
            pdf.ln(60)
    
    def add_event_details(pdf, date, description):
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, f'Date: {date}', align = 'C', ln=1)
        pdf.ln(5)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, description)
        pdf.ln(10)

    def add_section(pdf, content):
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, content)
        pdf.ln(10)
        
        # Agenda functions #
    def add_agenda_item(pdf, title, time, abstract):        
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, title, ln=1)
        pdf.cell(0, 10, time, ln=1)
        pdf.ln(5)
        pdf.set_font('Arial', '', 11)
        pdf.multi_cell(0, 10, abstract)
        pdf.ln(10)
         
    def add_speaker_list(pdf, name, title, company):
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, name, ln=1)
        pdf.cell(0, 10, title, ln=1)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, company, ln=1)
        pdf.ln(10)

 
 
