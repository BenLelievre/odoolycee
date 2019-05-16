# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tdsiiutclass(models.Model):
     _name = 'iut.class'

     name = fields.Char("Nom classe", required=True)
     level = fields.Selection(string="Niveau", selection=[('seconde', 'Seconde'),  ('premiere', 'Première'), ('terminale', 'Terminale')], required=True)
     teacher_ids = fields.Many2many('res.partner', string='Professeurs')
     student_nb = fields.Integer(compute='_compute_total',string="Nombre d'élèves")
     student_ids = fields.One2many('iut.student','class_id', string='Elèves')
     schedule_ids = fields.One2many('iut.schedule','class_id', string='Agenda')
    
     @api.depends('student_nb')
     def _compute_total(self):
        for record in self:
            a=self.env['iut.student'].search([('class_id',"=", record.id)])
            record.student_nb = len(a) 