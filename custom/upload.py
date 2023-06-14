import psycopg2
import base64
import os

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="acs_recruitment",
    user="odoo",
    password="hoa123456"
)

# Get a list of PDF files in a folder
pdf_folder = '/home/hoanguyen/Desktop/test/'
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

# Loop through the PDF files and insert them into the database
for pdf_file in pdf_files:
    # Read the PDF file as binary data
    with open(os.path.join(pdf_folder, pdf_file), 'rb') as f:
        pdf_data = f.read()

    # Encode the binary data as a base64 string
    pdf_data_encoded = base64.b64encode(pdf_data).decode('utf-8')

    # Insert the base64 string into the PostgreSQL database
    cur = conn.cursor()
    cur.execute("INSERT INTO store_pdf (pdf_data) VALUES (%s)", (pdf_data_encoded,))
    conn.commit()