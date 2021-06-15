class Persona:

	def __init__(self, nombre):
		self.nombre = nombre

	def avanza(self):
		print('Ando caminando')

class Ciclista(Persona): # Clase ciclista extiende persona

	def __init__(self, nombre):
		super().__init__(nombre)  # Herencia

	def avanza(self):
		print('Ando moviendome en  mi bicicleta')


def main():
	persona = Persona('David')
	persona.avanza()

	ciclista = Ciclista('Daniel')
	ciclista.avanza()


if __name__ == '__main__':
	main()
