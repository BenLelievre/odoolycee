# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class tdsiiutschedule(models.Model):
     _name = 'iut.schedule'
     _order = 'Date_start'

     Date_start = fields.Datetime("Horaire début", required=True)
     Date_stop = fields.Datetime("Horaire fin", required=True)
     room = fields.Char("Salle de classe")
     class_id = fields.Many2one('iut.class', string='Classe', required=True)
     course_id = fields.Many2one('iut.course', string='Cours')
