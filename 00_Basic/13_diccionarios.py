# def run():
# 	mi_diccionario = {
# 		"llave1": 1,
# 		"llave2": 2,
# 		"llave3": 3,
# 	}
# 	print(mi_diccionario)  # {'llave1': 1, 'llave2': 2, 'llave3': 3}

# 	print(mi_diccionario["llave1"]) # 1

# 	for llave in mi_diccionario.keys():  # Imprime lista de llaves
# 		print(llave)

# 	for valor in mi_diccionario.values():   # Imprime los valores 
#  		print(valor)





mi_diccionario = {
		"llave1": 1,
		"llave2": 2,
		"llave3": 3,
	}
# list out keys and values separately
lista_llaves = list(mi_diccionario.keys())
print(lista_llaves)

lista_valores = list(mi_diccionario.values())
print(lista_valores)
 
# print key with val 2
posicion = lista_valores.index(2)
print(lista_llaves[posicion])


# function to return key for any value
def acceder_llave(val):
    for llave, valor in mi_diccionario.items():
         if val == valor:
             return llave
 
    return "La llave no existe"

print(acceder_llave(3))


# def run():
# 	poblacion_paises = {
# 		"Argentina": 44938712,
# 		"Brasil": 210147125,
# 		"Colombia": 50372424
# 	}
# 	print(poblacion_paises["Brasil"])


# 	for pais in poblacion_paises.keys():
# 		print(pais)

# 	for pais in poblacion_paises.values():
# 		print(pais)

# 	for pais, poblacion in poblacion_paises.items():
# 		print(pais + " tiene " + str(poblacion) + " habitantes")
# 		# print(pais, poblacion)


# if __name__ == "__main__":
# 	run()
