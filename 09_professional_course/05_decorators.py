def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original.")
        func()
    return envoltura

@decorador # Sugar sintax
def saludo():
    print("¡Hola!")

saludo()