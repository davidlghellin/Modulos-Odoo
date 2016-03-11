# -*- coding: utf-8 -*-
from openerp import models,fields,api
class BonosModel(models.Model):
        _name = 'bonos.model'
        nbonos = fields.Integer('Número de bonos',required=True)
	clienteID = fields.Many2one('cliente.model',string='Cliente asociado',required=True)
	usos = fields.Text('Días que se ha usado los bonos')




#función que decrementa el número de bonos y apunta cuando se han usado
	@api.one
	def decrementar_bono(self):
		if self.nbonos>0:
			self.nbonos = self.nbonos - 1
			self.usos = str(fields.Date.today()) + str(self.usos)
#               self.usos = fields.Date.today()
		return True
