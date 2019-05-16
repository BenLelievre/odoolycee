# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tdsiiutrespartner(models.Model):
     _name = 'res.partner'
     _inherit ='res.partner'
     _order = 'name'
     class_ids = fields.Many2many('iut.class', string='Classes')