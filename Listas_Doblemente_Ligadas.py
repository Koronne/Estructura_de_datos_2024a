from Nodo4 import Node

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
        if self.isEmpty():
            self.head = self.tail = new_node
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
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                self.counter += 1
                break
            current = current.next

    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
        new_node = Node(val)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.counter += 1

    def headDelete(self) -> None:
        ''' Eliminar el primer elemento de la lista '''
        if not self.isEmpty():
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.counter -= 1

    def tailDelete(self) -> None:
        ''' Eliminar el último elemento de la lista '''
        if not self.isEmpty():
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
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
                break
            current = current.next

    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''
        current = self.head
        while current:
            print(current)
            current = current.next

# Ejemplo de uso
if __name__ == '__main__':
    lista_doblemente_ligada = DoubleLinkedList()

    # Llenado de la lista
    for item in [1, 2, -212, True, 'UNE', 3]:
        lista_doblemente_ligada.tailInsert(item)

    # Impresión de la lista
    print('Impresión #1 -> Llenado de lista')
    lista_doblemente_ligada.traverse()

    # Adición de un nuevo elemento al final
    print('\nImpresión #2 -> Nuevo elemento al final')
    n = False
    lista_doblemente_ligada.tailInsert(n)
    lista_doblemente_ligada.traverse()

    # Adición de un nuevo elemento al inicio
    print('\nImpresión #3 -> Nuevo elemento al inicio')
    n = 'Estructuras'
    lista_doblemente_ligada.headInsert(n)
    lista_doblemente_ligada.traverse()

    # Adición de elemento entre dos nodos
    print('\nImpresión #4 -> Nuevo elemento entre dos nodos')
    prev, n = True, False
    lista_doblemente_ligada.insertBetween(prev, n)
    lista_doblemente_ligada.traverse()

    # Eliminación del primer elemento e impresión
    print('\nImpresión #5 -> Eliminación del primer elemento')
    lista_doblemente_ligada.headDelete()
    lista_doblemente_ligada.traverse()
    
    # Eliminación del último elemento e impresión
    print('\nImpresión #6 -> Eliminación del último elemento')
    lista_doblemente_ligada.tailDelete()
    lista_doblemente_ligada.traverse()
    
    # Eliminación del primer elemento e impresión
    print('\nImpresión #7 -> Eliminación de elemento en la lista')
    n = 3
    lista_doblemente_ligada.deleteBetween(n)
    lista_doblemente_ligada.traverse()