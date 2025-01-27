from flask import Flask, jsonify, request
import psycopg2
import json
from docx import Document
from fpdf import FPDF

app = Flask(__name__)

# Database connection
conn = psycopg2.connect(
    dbname="master",
    user="postgres",
    
    password="xFl201X20FabSN2024Nov",
    host="localhost",
    port="5432"
)

@app.route('/users', methods=['GET'])
def get_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mock_speaker_data;")
    rows = cursor.fetchall()
    return jsonify(rows)

data = get_users()
print(data)

if __name__ == "__main__":
    app.run(debug=True)