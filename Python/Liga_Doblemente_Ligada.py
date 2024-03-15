from Nodo6 import Node

class DoubleLinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        self.counter: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def isEmpty(self) -> bool:
        ''' Mostrar si la lista está vacía '''
        return self.counter == 0

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.counter += 1

    def insertBetween(self, prev_val, val) -> None:
        ''' Insertar elemento entre dos nodos '''
        new_node = Node(val)
        current = self.head

        while current:
            if current.val == prev_val:
                new_node.prev = current
                new_node.next = current.next

                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node

                current.next = new_node
                self.counter += 1
                return

            current = current.next

        print(f'Error: Nodo con valor {prev_val} no encontrado')

    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
        new_node = Node(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.counter += 1

    def headDelete(self) -> None:
        ''' Eliminar el primer elemento de la lista '''
        if not self.head:
            print('Error: La lista está vacía')
            return

        if self.head.next:
            self.head.next.prev = None
        else:
            self.tail = None

        self.head = self.head.next
        self.counter -= 1

    def tailDelete(self) -> None:
        ''' Eliminar el último elemento de la lista '''
        if not self.tail:
            print('Error: La lista está vacía')
            return

        if self.tail.prev:
            self.tail.prev.next = None
        else:
            self.head = None

        self.tail = self.tail.prev
        self.counter -= 1

    def deleteBetween(self, val) -> None:
        ''' Eliminar elemento entre dos nodos '''
        current = self.head

        while current:
            if current.val == val:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.counter -= 1
                return

            current = current.next

        print(f'Error: Nodo con valor {val} no encontrado')

    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''
        current = self.head
        while current:
            print(current)
            current = current.next

if __name__ == '__main__':
    lista_doblemente_ligada = DoubleLinkedList()

    # Llenado de la lista
    for elem in [1, 2, -212, True, 'UNE', 3]:
        lista_doblemente_ligada.tailInsert(elem)

    # Impresión de la lista
    print('Impresión #1 -> Llenado de lista')
    lista_doblemente_ligada.traverse()

    # Adición de un nuevo elemento al final
    print('\nImpresión #2 -> Nuevo elemento al final')
    lista_doblemente_ligada.tailInsert(False)
    lista_doblemente_ligada.traverse()

    # Adición de un nuevo elemento al inicio
    print('\nImpresión #3 -> Nuevo elemento al inicio')
    lista_doblemente_ligada.headInsert('Estructuras')
    lista_doblemente_ligada.traverse()

    # Adición de elemento entre dos nodos
    print('\nImpresión #4 -> Nuevo elemento entre dos nodos')
    lista_doblemente_ligada.insertBetween(True, False)
    lista_doblemente_ligada.traverse()

    # Eliminación del primer elemento e impresión
    print('\nImpresión #5 -> Eliminación del primer elemento')
    lista_doblemente_ligada.headDelete()
    lista_doblemente_ligada.traverse()
    
    # Eliminación del último elemento e impresión
    print('\nImpresión #6 -> Eliminación del último elemento')
    lista_doblemente_ligada.tailDelete()
    lista_doblemente_ligada.traverse()
    
    # Eliminación de un elemento en la lista e impresión
    print('\nImpresión #7 -> Eliminación de elemento en la lista')
    lista_doblemente_ligada.deleteBetween(3)
    lista_doblemente_ligada.traverse()