menu = """
Bienvenido al conversor de monedas 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
	cop = float(input("Cuantos pesos colombianos tienes: "))
	valor_usd = 3875
	usd = round((cop / valor_usd), 2)
	usd = str(usd)
	print("Tienes $ " + usd + " dolares")
elif opcion == 2:
	ars = float(input("Cuantos pesos argentinos tienes: "))
	valor_usd = 76.16
	usd = round((ars / valor_usd), 2)
	usd = str(usd)
	print("Tienes S " + usd + " dolares")
elif opcion == 3:
	mxn = float(input("Cuantos pesos mexicanos tienes: "))
	valor_usd = 22.08
	usd = round((mxn / valor_usd), 2)
	usd = str(usd)
	print("Tienes $ " + usd + " dolares")
else:
	print("Ingresa una opcion correcta")
