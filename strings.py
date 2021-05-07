def run():
	name = input("Cual es tu nombre? ")
	greeting = f'Hola, {name}!'
	print(f'{greeting} El tamano del saludo fue de: {str(len(greeting))} caracteres')

if __name__ == "__main__":
	run()


# variable.upper() = 'todos los caracteres en MAYÚSCULAS'
# variable.capitalize() = 'solo la primera en MAYÚSCULA'
# variable.lower() = 'todos los caracteres en minúscula'
# variable.strip() = 'eliminar espacios basura del string'
# variable.replace('caractera a cambiar', 'caracter por poner') = remplazar caracter