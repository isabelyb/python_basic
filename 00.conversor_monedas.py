 


cop = input("Cuantos pesos colombianos tienes?")
cop = float(cop)
valor_usd = 3875
usd = cop / valor_usd
usd = round(usd, 2)
usd = str(usd)
print("Tienes $" + usd + " USD")

dolar = input("Cuantos dolares tienes?")
dolar = float(dolar)
valor_dolar = 3875
pesos = dolar * valor_dolar
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos colombianos")
