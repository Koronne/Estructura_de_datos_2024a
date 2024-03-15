''' Implementación de nodo versátil para listas doblemente ligadas '''

class Node:
    def __init__(self, val = None):
        ''' Inicializador '''
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        prev_value = self.prev.val if self.prev else None
        next_value = self.next.val if self.next else None
        return f'Nodo con valor {self.val}\nAnterior {prev_value}\nSiguiente {next_value}'