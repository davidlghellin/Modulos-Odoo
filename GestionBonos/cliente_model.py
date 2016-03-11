# -*- coding: utf-8 -*-
from openerp import models,fields
class ClienteModel(models.Model):
        _name = 'cliente.model'
        nombre = fields.Char('Nombre del cliente',required=True)
        direccion = fields.Char('Dirección')
        telefono = fields.Char('Telefono del cliente',required=True)
        bonos = fields.One2many('bonos.model','clienteID',string='Bonos')

