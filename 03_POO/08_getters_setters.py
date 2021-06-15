# Python los getters y setters tienen el objetivo de asegurar el encapsulamiento de datos.


# clase que almacena un dato de distancia recorrida en millas (mi) y lo convierte a kilómetros (km):
class Millas:
	def __init__(self, distancia = 0):
		self.distancia = distancia

	def convertir_a_kilometros(self):
		return (self.distancia * 1.609344)

# Objeto que haga referencia a un viaje:

# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

# Obtenemos el atributo distancia
print(avion.distancia) #200

# Obtenemos el método convertir_a_kilometros
print(avion.convertir_a_kilometros()) # 321.8688


'''Utilizando getters y setters
Incluyamos un par de métodos para obtener la distancia y otro para que no acepte valores inferiores a cero, pues no tendría sentido que un vehículo recorra una distancia negativa.
'''

class Millas:
	def __init__(self, distancia = 0):
		self.distancia = distancia

	def convertir_a_kilometros(self):
		return (self.distancia * 1.609344)

	# Método getter
	def obtener_distancia(self):
		return self._distancia

	# Método setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		self._distancia = valor

'''El método getter obtendrá el valor de la distancia que y el método setter se encargará de añadir una restricción. También debemos notar cómo distancia fue reemplazado por _distancia, denotando que es una variable privada.

Si probamos nuestro código funcionará, la desventaja es que cualquier aplicación que hayamos creado con una base similar deberá ser actualizado. Esto no es nada escalable si tenemos cientos o miles de líneas de código.
'''