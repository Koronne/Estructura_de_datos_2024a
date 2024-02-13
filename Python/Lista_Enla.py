''' Implementación de lista ligada '''
from Nodo4 import Node

class LinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        self.counter:int = 0
        self.head:Node|None = None
        self.tail:Node|None = None

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
        nuevo_nodo = Node(val)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo
        self.counter += 1

    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
        if self.tail == None:
            self.headInsert(val)
            self.tail = self.head
            return
        
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.counter += 1
    
    
    def headRemove(self) -> None:
        ''' Remover el elemento al inicio de la lista '''
        if self.head is None:
            raise ValueError('La lista esta vacia')
        
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.counter -=1

    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''

        if not self.head:
            print('La lista esta vacia')
            return
        
        nuevo_nodo = self.head
        cnt = 1
        while nuevo_nodo is not None:
            print(f'Nodo #{cnt} -> {nuevo_nodo.next}')
            nuevo_nodo = nuevo_nodo.next

if __name__ == '__main__':
    lista_ligada = LinkedList()

    # Genera tus casos de prueba con la siguiente lista
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

    # Llenado de la lista
    for i in lista_tradicional:
        lista_ligada.headInsert(i)
    ...

    # Impresión de la lista
    ...

    # Adición de un nuevo elemento al final
    n = False
    ...

    # Adición de un nuevo elemento al inicio
    n = 'Estructuras'
    ...

    # Eliminación del primer elemento e impresión
    ...

    # Eliminación del último elemento (o explica por qué no es posible en un comentario multilínea)

    ''' Manejo de errores

    # Ejemplo de invocación de errores
    raise ValueError('La lista está vacía')

    # Ejemplo de manejo de errores
    try:
        print(1/0)
    except (ZeroDivisionError, ValueError) as identificador:
        print(f'Intentaste dividir entre 0 DX ({identificador})')
    except Exception as e:
        print('Error inesperado')
    finally:
        print('Saliendo...')

    '''