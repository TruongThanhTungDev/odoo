from odoo import api, fields, models

class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Student management"

    name = fields.Char(string="Họ và tên", required=True)
    birthday = fields.Date(string="Ngày sinh", required=True)
    class_id = fields.Many2one("class.information", string="Lớp", required=True)