''' Modulo de contenedor de clase Nodo para listas ligadas '''

class Nodo:
    '''Creacion de Nodo'''

    def __init__(self, val: int = None):
        '''Inicializacion de clase'''
        self.val = val
        self.next = None

    def __str__(self) -> str:
        if self.val:
            return f'Valor del Nodo = {self.val}'

        return f'El nodo no tiene valor'