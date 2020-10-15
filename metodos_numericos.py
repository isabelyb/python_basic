
def run():
	print('Vamos a calular raices cuadradas')
	numero = int(input('Digita un numero: '))
	metodo = input("""Selecciona el metodo por el que quieres calcular tu raiz cuadrada:
				a: Numeracion Exhaustiva (Solo raices exactas)
				b: Busqueda Binaria
				c: Aproximacion numerica
			""")

	if metodo == 'a':
		num_exh(numero)
	elif metodo == 'b':
		bus_bin(numero)
	elif metodo == 'c':
		aprox(numero)
	else:
		print('Selecciona un metodo valido')


def num_exh(numero):
	resultado = 0

	while resultado ** 2 < numero:
		resultado += 1
	if resultado ** 2 == numero:
		print(f'La raiz cuadrada de {numero}, calculada por el metodo de numeracion exhaustiva es: {resultado}')
	else:
		print(f'{numero} no tiene una raiz cuadrada exacta')


def bus_bin(numero):
	epsilon = 0.01
	bajo = 0.0
	alto = max (1.0, numero)
	resultado = (alto + bajo) / 2

	while abs(resultado**2 - numero) >= epsilon:
		if resultado**2 < numero:
			bajo  = resultado
		else:
			alto = resultado
		resultado = (alto + bajo) / 2
	print(f'La raiz cuadrada de {numero} calculada por el metodo de Busqueda Binaria es: {resultado}')


def aprox(numero):
	epsilon = 0.01
	paso = epsilon**2
	resultado = 0.0

	while abs(resultado**2 - numero) >= epsilon and resultado <= numero:
		resultado += paso
	if abs(resultado**2 - numero) >= epsilon:
		print(f'No se encontro la raiz cuadrada de {numero} por el metodo de aproximacion')
	else:
		print(f'La raiz cuadrada de {numero} calculada por el metodo de aproximacion es: {resultado}')



if __name__=='__main__':
	run()

