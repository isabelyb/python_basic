import random

def generar_contrasena():
	mayusculas = ["A", "B", "C", "D"]
	minusculas = ["a",  "b", "c", "d"]
	simbolos = ["!", "$", "&", "~"]
	numeros =  ['1', '2', '3', '4']

	caracteres = mayusculas +  minusculas + simbolos + numeros

	contrasena = []

	for i in range(10):
		caracter_random = random.choice(caracteres)
		contrasena.append(caracter_random)

	contrasena = "".join(contrasena)
	return contrasena


def run():
	contrasena = generar_contrasena()
	print ("Tu nueva contrasena es: " + contrasena )

if __name__ == "__main__":
	run()
