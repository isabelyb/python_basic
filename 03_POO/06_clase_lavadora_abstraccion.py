class Lavadora:

	def __init__(self): # puede dejarse sin cuerpo, así solo servirá para inicializar la clase
		pass

	def lavar(self, temperatura='fría'):
		self._llenar_tanque_de_agua(temperatura) #variables privadas, que son necesarias pero no se tiene que mostrar
		self._anadir_jabon()
		self._lavar()
		self._centrifugar()

	def _llenar_tanque_de_agua(self, temperatura):
		print(f'1. Llenando tanque con agua {temperatura}')

	def _anadir_jabon(self):
		print('2. Anadiendo jabón')

	def _lavar(self):
		print('3. Lavando')

	def _centrifugar(self):
		print('4. Centrifugando')

if __name__ == '__main__':
	lavadora = Lavadora()
	lavadora.lavar()
