def mayusculas(func):  # Un decorador es una función que recibe como parámetro
    def envoltura(texto): #  otra función, 
        return func(texto).upper()  # le añade cosas y
    return envoltura # retorna una función diferente.

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('Isa'))

# ISA, RECIBISTE UN MENSAJE 