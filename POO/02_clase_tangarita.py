
# Clase: Tangaritas

class tangarita:

    #atributos
    def __init__(self, especie, alimento):
        self.especie = especie
        self.alimento = alimento

    #métodos
    def comer(self):
        if self.alimento == 'frutas':
            tipo = 'frujívora'
        elif self.alimento == 'insectos':
            tipo = 'insectívora'
        else:
            tipo = 'Omnivora'
        return print(f'La Tangarita {self.especie} es {tipo}\n-------------------')

# instancias

multicolor = tangarita('Multicolor','frutas')
multicolor.comer()

golondrina = tangarita('Golondrina', 'insectos')
golondrina.comer()

rastrojera = tangarita('Rastrojera', 'frutas, insectos')
rastrojera.comer()
