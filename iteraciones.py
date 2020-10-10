contador = 0

while contador <= 10:
	print(contador)
	contador += 1

contador_ext = 0
contador_int = 0

while contador_ext < 5:
	while contador_int < 6:
		print(contador_ext, contador_int)
		contador_int += 1
	contador_ext += 1
	contador_int = 0
