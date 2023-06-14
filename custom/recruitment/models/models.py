from odoo import models, fields

class Recruitment(models.Model):
    _name = 'hr.recruitment'
    _description = 'ACS HR Recruitment'

    name = fields.Char(string='Name', required=True)
    detail = fields.Char(string='Detail', required=True)