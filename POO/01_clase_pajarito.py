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
        elif tipo_alimento == 'frutas':
            self.comer = 'frugívoro'    
        elif tipo_alimento == 'insectos':
            self.comer = 'insectívoro'
        elif tipo_alimento == 'carne':
            self.comer = 'carnívoro'    
        else:
            self.comer = 'nectívoro'
        return print(f'Su método de alimentacion es {self.comer}')    

    def informacion(self):
        print(f"El {self.nombre} es de color {self.color} y es del orden {self.orden}")

    def volar(self):
        if self.orden == 'Paseriformes' or self.orden == 'Piciformes':
            comportamiento = 'volador'
        else:
            comportamiento = 'no volador'
        return print(f'Tiene un comportamiento {comportamiento}\n-------------------')

       
# Instancias de Pájaritos
    
azuleji = pajarito('Azulejo', 'Azul', 'Paseriformes')
azuleji.informacion()
azuleji.comer('frutas')
azuleji.volar()

carpinteri = pajarito('Carpintero', 'Rojito y pintadito negro y blanco', 'Piciformes')
carpinteri.informacion()
carpinteri.comer('insectos')
carpinteri.volar()

pingui = pajarito('Pinguino', 'Banco y negro', 'Sphenisciformes')
pingui.informacion()
pingui.comer('carne')
pingui.volar()
