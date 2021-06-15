class Rectangulo:

	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	def area(self):
		return self.base * self.altura

class Cuadrado(Rectangulo): # La clase cuadrado extiende rectángulo

	def __init__(self, lado):
		super().__init__(lado, lado) # referencia directa de la superclase


if __name__ == '__main__':
	rectangulo = Rectangulo(base=3, altura=4)
	print(rectangulo.area())

	cuadrado = Cuadrado(lado=5)   # Hereda este método de la superclase
	print(cuadrado.area())
