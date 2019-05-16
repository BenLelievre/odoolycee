# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime,date
from dateutil.relativedelta import relativedelta

class tdsiiutstudent(models.Model):
     _name = 'iut.student'
     _order = 'firstname'

     firstname = fields.Char("Prènom", required=True)
     name = fields.Char("Nom", required=True)
     birthdate = fields.Date("Date de naissance", required=True)
     age = fields.Integer(compute='_calcul_age',string="Age")# C'est un champ compute
     class_id = fields.Many2one('iut.class', string='Classe')
     
     @api.depends('birthdate')
     @api.multi
     def _calcul_age(self):
        for record in self:
                if record.birthdate and record.birthdate <= fields.Date.today():
                    record.age = relativedelta(
                        fields.Date.from_string(fields.Date.today()),
                        fields.Date.from_string(record.birthdate)).years 
                else: 
                    record.age = 0