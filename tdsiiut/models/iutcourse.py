# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tdsiiutcourse(models.Model):
     _name = 'iut.course'
     _order = 'name'

     name = fields.Char("Nom cours")
