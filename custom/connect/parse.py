import psycopg2
from odoo import models, fields, api

# Connect to database
conn = psycopg2.connect(
    host="localhost",
    database="acs_recruitment",
    user="odoo",
    password="hoa123456"
)

cur = conn.cursor()
cur.execute("SELECT name, detail FROM recruitment")
records = cur.fetchall()
cur.close()
conn.close()

odoo_env = api.Environment(
    cur, 1, {}
)

class MyModel(models.Model):
    _name = 'my.module'
    name = fields.Char(string='name')
    email = fields.Char(string='detail')

for record in records:
    values = {
        'name': record[1],
        'detail': record[2]
    }
    my_model = odoo_env['my.module'].create(values)