# -*- coding: utf-8 -*-
from openerp import models,fields
class ProgramasOnline(models.Model):
        _name = 'programas.online'
        nombre = fields.Char('Nombre de la aplicación',required=True)
        lenguaje = fields.Selection([('C','C'),('C++','C++'),('Java','Java'),('Scala','Scala'),('Python','Python')],'Lenguaje de programación')
        precio = fields.Float('Precio')
        version = fields.Integer('Versión')
        fecha = fields.Date('Fecha de modificación')
        descripcion = fields.Text('Descripción')
        finalizada = fields.Boolean('Finalizada')
        fichero = fields.Char('Fichero con el código fuente')
        codigo = fields.Binary('Código de la aplicación')

#función que incrementa el número de versión actual y establece la fecha actual
	@api.one
	def aumentar_version(self):
		self.version = self.version + 1
		self.fecha = fields.Date.today()
		return True

#función que marca como finalizada (en caso de no estar finalizada)
	@api.one
	def marcar_finalizada(self):
		if not self.finalizada:
			self.finalizada=True
		return True
