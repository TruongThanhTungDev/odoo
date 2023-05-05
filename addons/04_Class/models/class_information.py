from odoo import api, fields, models

class ClassInformation(models.Model):
    _name = "class.information"
    _description = "Class management"

    name = fields.Char(string="Tên lớp", required=True)
    grade = fields.Char(string="Khối", required=True)
    mainTeacher = fields.Char(string="GVCN", required=True)
    school_id = fields.Many2one("school.information", string="Trường", required=True)