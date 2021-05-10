def conversor(moneda, valor_usd):
	cop = float(input("Cuantos pesos " + moneda + " colombianos tienes: "))
	usd = round((cop / valor_usd), 2)
	usd = str(usd)
	print("Tienes $ " + usd + " dolares")


menu = """
Bienvenido al conversor de monedas 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
	conversor("colombianos", 3875)
elif opcion == 2:
	conversor("argentinos", 65)
elif opcion == 3:
	conversor("mexicanos", 24)
else:
	print("Ingresa una opcion correcta")
