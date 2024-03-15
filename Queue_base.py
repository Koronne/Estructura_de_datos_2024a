''' Implementación de Queue (Cola) '''
# No se necesita ListaDinamica para esta implementación

class Empty(Exception):
    ''' Error genérico para contenedores vacíos '''

class Queue:
    ''' Clase implementadora de queue '''
    DEFAULT_CAPACITY = 15

    def __init__(self) -> None:
        ''' Crear una queue vacía '''
        self.__data = [None] * Queue.DEFAULT_CAPACITY
        self.__size = 0
        self.__front = 0

    def __len__(self) -> int:
        ''' Regresa el número de elementos dentro de la queue '''
        return self.__size
    
    def __str__(self) -> str:
        ''' Representación en cadena de la clase '''
        holder = []

        for i in range(self.__size):
            holder.append(str(self.__data[(self.__front + i) % len(self.__data)]))
        
        return f'[{", ".join(holder)}]\nFrente de la queue en {self.__front}'
    
    def is_empty(self) -> bool:
        ''' Indica si la queue está vacía '''
        return self.__size == 0
    
    def first(self) -> object:
        ''' Muestra el primer elemento en la queue '''
        if not self.__size:
            raise Empty('Queue vacía')

        return self.__data[self.__front]
    
    def dequeue(self) -> object:
        ''' Retorna el primer elemento de la queue '''
        if not self.__size:
            raise Empty('Queue vacía')

        holder = self.__data[self.__front]

        self.__front = (self.__front + 1) % self.__size
        self.__size -= 1

        if 0 < self.__size <= len(self.__data) // 4:
            self.__resize(len(self.__data) // 2)

        return holder
    
    def enqueue(self, e) -> None:
        ''' Agrega un elemento a la queue '''
        # TODO: Fix this
        if self.__size == len(self.__data):
            self.__resize(2 * self.__size)
        
        insert_place = (self.__front + self.__size) % len(self.__data)
        self.__data[insert_place] = e
        self.__size += 1

    def __resize(self, n_size) -> None:
        ''' Aumenta la capacidad del arreglo interno '''
        # TODO: Fix this
        prev = self.__data
        self.__data = [None] * n_size
        walk = self.__front

        for i in range(self.__size):
            self.__data[i] = prev[walk]
            walk = (walk + 1) % len(prev)
        
        self.__front = 0
    
if __name__ == '__main__':
    ''' Pruebas locales de la clase '''
    q = Queue()

    for i in range(1, 101, 2):
        q.enqueue(i)
    
    print(q)

    q.dequeue()
    print(q)

    print(q.first())
    print(q.is_empty())