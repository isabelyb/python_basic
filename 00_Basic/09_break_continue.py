# continue

# def run():
# 	for contador in range(10):
# 		if contador % 2 != 0:
# 			continue #el bloque no se ejecuta y continua la variable
# 		print (contador)

# break

# def run():
# 	for i in range(10):
# 		print(i)
# 		if i == 8:
# 			break # aqui para el codigo

def run():
	texto = input("Escribe un texto: ")
	for letra in texto:
		if letra == "o":
			break
		print(letra)

if __name__ == "__main__":
	run()
