''' Implementación de nodo versátil para listas ligadas '''

class Node:
    def __init__(self, val = None):
        ''' Inicializador '''
        self.val = val
        self.next = None