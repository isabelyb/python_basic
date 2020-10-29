
class Estudiante(object):
	def __init_(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def hola(self):
		return 'Mi nombre es %s y tengo %i' % (self.nombre, self.edad)

e = Estudiante('Isabely', 37)
print e.hola()

#Should be print 'Mi nombre es Isabely y tengo 37', pero no funciona....
