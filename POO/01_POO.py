# Clase Pajarito

class pajarito:
    # Atributos de pajarito
    def __init__(self, nombre, color, orden):
        self.nombre = nombre
        self.color = color
        self.orden = orden


    # Métodos de pajarito    
    def comer(self, tipo_alimento):
        if tipo_alimento == 'semillas':
            self.comer = 'granívoro'
        else:
            self.comer = 'nectívoro'
        return self.comer    

    def informacion(self):
        print(f"{self.nombre}\n{self.color}\n{self.orden}")

    def volar(self):
        if self.orden == 'Paseriformes':
            comportamiento = 'volador'
        else:
            comportamiento = 'no volador'
        return comportamiento

       
#tipo_alimento = ['semillas', 'frutas', 'insectos', 'carne', 'nectar']
    
azuleji = pajarito('Azulejo', 'Azul', 'Paseriformes')
azuleji.informacion()
print(azuleji.comer('semillas'))
print(azuleji.volar())