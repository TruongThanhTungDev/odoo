from odoo import models, fields, api
import psycopg2

# Connect to database
conn = psycopg2.connect(
    host="localhost",
    database="acs_recruitment",
    user="odoo",
    password="hoa123456"
)

cur = conn.cursor()

odoo_env = api.Environment(
    cur, 1, {}
)

# Ger records
records = odoo_env['my.module'].search([])

for record in records:
    query = f"UPDATE recruitment SET detail ='{record.detail}' WHERE name={record.name}"
    cur.execute(query)

conn.commit()
cur.close()
conn.close()