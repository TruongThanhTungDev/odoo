from odoo import api, fields, models

class SchoolInformation(models.Model):
    _name = "school.information"
    _description = "School management"

    name = fields.Char(string="Tên trường")
    type = fields.Selection([('private', 'Dân lập'), ('public', 'Công lập')], default='public', string="Loại trường")
    email = fields.Text(string="Email")
    address = fields.Text(string="Địa chỉ")
    phone = fields.Char(string="Số điện thoại")
    isOnline = fields.Boolean(string="Online?")
    rank = fields.Integer(string="Xếp hạng")
    establishDay = fields.Date(string="Ngày thành lập")
    document = fields.Binary(string="Tài liệu")
    document_name = fields.Char(string="Tên tài liệu")