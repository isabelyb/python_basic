#num_1 = int(input('Escoge un entero: '))
#num_2 = int(input('Escoge otro entero: '))

#if num_1 > num_2:
#	print('El primero es mayor que el segundo')
#elif num_1 < num_2:
#	print('El segundo numero es mayor que el primero')
#else:
#	print('Los dos numeros son iguales')


compare_age = input('Vamos a comparar la edad de dos personas y te voy a decir quien es mayor. Estas listo? y(si) n(no)')

if compare_age == "y":
	name_1 = input('Quien es la primera persona? ')
	age_1 = int(input(f'Que edad tiene {name_1}? '))

	name_2 = input('Quien es la segunda persona? ')
	age_2 = int(input(f'Que edad tiene {name_2}? '))


	if age_1 > age_2:
		print(f'{name_1} es mayor que {name_2}')
	elif age_1 < age_2:
		print(f'{name_2} es mayor que {name_1}')
	else:
		print(f'{name_1} y {name_2} tienen la misma edad')

elif compare_age == "n":
	print('Ok. Vuelve pronto')

else:
	print('elige una opcion correcta')
