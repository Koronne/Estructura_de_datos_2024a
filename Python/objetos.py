#class Animal(ClasePadre) -> Para poder llamarlo en otro lado
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad = 0
        self.color = ''

    def __str__(self) -> str:
        #f'' = f-string
        return f'Me llamo {self.nombre}'
    #return 'Me llamo' + str(self.nombre)

#dunder = double under methods
#help(int)
if __name__ == '__main__':
    print('Practica')