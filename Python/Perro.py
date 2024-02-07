from objetos import Animal

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def ladrar(self):
        print('Woof')


if __name__ == '__main__':
    perro = Animal('Cookie')
    #print(perro)

    perro = Perro('Churru')
    print(perro)
    perro.ladrar()