class Node:
    def __init__(self, val=None):
        ''' Inicializador '''
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        if self.val:
            return f'Nodo con valor: {self.val}'
        
        return f'El nodo no tiene valor'