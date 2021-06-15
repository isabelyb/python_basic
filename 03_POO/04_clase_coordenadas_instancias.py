
'''√[(x_1 - x_2)^2 + (y_1 + y_2)^2]
Para calcular la distancia entre dos puntos, utilizando sus coordenadas.
'''
class Coordenada:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distancia(self, otra_coordenada): # otra_coordenada es otra instancia de la clase coordenada
		x_diff = (self.x - otra_coordenada.x)**2 # distancia entre coordenadas
		y_diff = (self.y - otra_coordenada.y)**2 # distancia entre coordenadas

		return (x_diff + y_diff)**0.5 # raiz cuadrada

if __name__ == '__main__':
	coord_1 = Coordenada(3, 30)
	coord_2 = Coordenada(4, 8)

	print(coord_1.distancia(coord_2))
	print(isinstance(coord_2, Coordenada)) # saber si coord_2 es instancia de la clase Coordenada
