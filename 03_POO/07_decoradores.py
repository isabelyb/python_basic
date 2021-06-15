# Analizar el siguiente código:
def funcion_decoradora(funcion): # Está llamando a funcion() que es -linea 16-
	def wrapper():  
		print("Este es el último mensaje...") # 1
		funcion() # la que le diga en la linea 16
		print("Este es el primer mensaje ;)\n-------------------") # 3
	return wrapper

def zumbido():
	print("Buzzzzzz")    # 2

def popito():
	print("tiene popito")    # 2


zumbihgfrydo = funcion_decoradora(popito)  # la función wrapper() recibe a la función zumbido() cómo parámetro y coloca su salida entre los otros dos prints.

zumbihgfrydo()

# Otra forma de escribirlo
@funcion_decoradora
def zumbido():
	print("Buzzzzzz")

zumbido()