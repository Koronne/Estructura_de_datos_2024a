''' Implementación de Stack (Pila) '''
from ListaDinamicaCompleta_base import ListaDinamica

class EmptyStack(Exception):
    ''' Error personalizado para stack vacío '''

class Stack:
    ''' Clase implementadora de stack '''

    def __init__(self) -> None:
        self.__S = ListaDinamica()

    def __str__(self) -> str:
         return str(self.__S)
    
    def __len__(self) -> int:
        '''Regresa el número de elementos dentro del stack '''
        return len(self.__S)

    def is_empty(self) -> bool:
        ''' Indica si el stack está vacío '''
        return len(self) == 0
    
    def push(self, e) -> None:
        ''' Agregar un elemento al stack '''
        self.__S.append(e)

    def top(self) -> object:
        ''' Regresa el elemento hasta el tope del stack sin eliminarlo '''
        if self.is_empty():
            raise EmptyStack('El stack esta vacia')
        
        return self.__S[-1]

    def pop(self) -> object:
        ''' Elimina el elemento hasta el tope del stack y lo regresa '''
        if self.is_empty():
            raise EmptyStack('El stack esta vacia')

        return self.__S.pop()

if __name__ == '__main__':
    '''Pruebas de la implementación '''
    S = Stack()
    secuencia = [1, 2, 3, 'A', 'B', False, True]

    for elem in secuencia:
        S.push(elem)

    print(f'Stack resultante -> {S}')
    print(f'El Stack esta vacio? -> {S.is_empty()}') 
    print(f'Elemento hasta arriba -> {S.top()}')
    print(f'Longitud original -> {len(S)}')
    print(f'Eliminacion del elemento hasta arriba -> {S.pop()}')
    print(f'Nueva longitud -> {len(S)}')
    print(f'Nueva representacion -> {S}\n')

    s_empty = Stack()
    print(f'Longitud del segundo stack -> {len(s_empty)}')
    try:
        print(f'Elemento hasta arriba -> {s_empty.pop()}')
    except EmptyStack as e:
        print(f'El stack esta vacia ({e} ({e} ({e} (Creo que el stack esta vacio))))')
    except:
        print('Un error inesperado ocurrio')