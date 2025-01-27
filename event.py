import datetime
import psycopg2
from fpdf import FPDF
from pdf_class import PDFclass


# Connect to PostgreSQL


class Event():  
    def get_event_data(cursor):
        query = "SELECT * FROM event where id = 1"
        cursor.execute(query)
        return cursor.fetchall()


# Close Database Connection
