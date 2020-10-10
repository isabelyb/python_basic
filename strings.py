def run():
	name = input("Cual es tu nombre? ")
	greeting = f'Hola, {name}!'
	print(f'{greeting} El tamano del saludo fue de: {str(len(greeting))} caracteres')

if __name__ == "__main__":
	run()
