''' Implementación de lista dinámica '''
from __future__ import annotations
import ctypes

'''
    Considerar el caso de múltiples remociones

    Decrementar el tamaño del arreglo a la mitad
    cada que la cantidad de elementos en el arreglo
    sea 1/4 de la capacidad actual
'''

class ListaDinamica:
    def __init__(self) -> None:
        ''' Inicializar un arreglo vacío '''
        self.__n = 0                          # Elementos actuales
        self.__c = 1                          # Capacidad inicial por defecto
        self.__A = self.__init_arr(self.__c)  # Arreglo contenedor
    
    def __Check_resize(decrease_func):
        ''' Decorador para revisar relación elementos/capacidad '''
        def inner(self, *args):
            if not (len(self)):
                raise IndexError('La lista esta vacia')
            
            val = decrease_func(self, *args)

            ''' Manejar resize aquí '''
            if self.__n <= self.__c // 4:
                self.__resize(self.__c // 2)

            return val

        return inner

    def __len__(self) -> int:
        ''' Regresa la cantidad de elementos almacenados en la lista '''
        return self.__n

    def __getitem__(self, k) -> object:
        ''' Regresa un elemento en una posición k '''
        if k < 0:
            if abs(k) > self.__n:
                raise IndexError(f'Índice inválido ({k})')
            k = self.__n + k
        elif k >= self.__n:
            raise IndexError(f'Índice inválido ({k})')
        
        return self.__A[k]
    
    def __contains__(self, obj) -> bool:
        ''' Revisa si la lista contiene a un objeto '''
        for i in range(self.__n):
            if self.__A[i] == obj:
                return True
                
        return False
    
    def __eq__(self, l:ListaDinamica) -> bool:
        ''' Revisa si dos listas son iguales '''
        if len(self) != len(l):
            return False
        

        for i in range(len(self)):
            if self.__A[i] != l[i]:
                return False
            
        return True
    
    def __ne__(self, l:ListaDinamica) -> bool:
        ''' Revisa si dos listas no son iguales '''
        return not self.__eq__(l)

    
    @__Check_resize
    def __delitem__(self, k) -> None:
        ''' Elimina un elemento de la lista '''

        for i in range(k , len(self)-1):
            self.__A[i] = self.__A[i+1]

        self.__n -= 1

    def __add__(self, l:ListaDinamica) -> ListaDinamica:
        ''' Agrega elementos al final de la lista y retorna una nueva '''
        holder = ListaDinamica()

        for i in range(len(self)):
            holder.append(self.__A[i])

        for i in range(len(l)):
            holder.append(l[i])

        return holder
    
    def __iadd__(self, l:ListaDinamica) -> ListaDinamica:
        ''' Agrega elementos al final de la lista (in-place) '''
        for i in range(len(l)):
            self.append(l[i])
        return  self
    
    def __str__(self) -> str:
        ''' Retorna la representación en cadena de la lista '''
        return '[' + ', '.join(str(self.__A[i]) for i in range(len(self))) + ']'

    def append(self, obj) -> None:
        ''' Añade un elemento al final de la lista '''
        if self.__n == self.__c:
            self.__resize(2 * self.__c)
        
        self.__A[self.__n] = obj
        self.__n += 1
    
    def count(self, obj) -> None:
        ''' Cuenta las instancias de un objeto dentro de la lista '''
        contador = 0 

        for i in range(len(self)):
            if self.__A[i] == obj:
                contador += 1

        return contador
    
    def index(self, obj) -> int:
        ''' Regresa la posición de la primera instancia de un
        objeto en una lista '''
        for i in range(len(self)):
            if self.__A[i] == obj:
                return i 
            
        raise ValueError[f'El objeto {obj} no esta en la lista']

    def insert(self, k, obj) -> None:
        ''' Inserta un objeto en la posición k de la lista '''
        if self.__n == self.__c:
            self.__resize(2 * self.__c)

        k  += len(self) if k < 0 else 0

        for i in range(len(self), k, -1):
            self.__A[i] = self.__A[i - 1]
        
        self.__A[k] = obj
        self.__n += 1

    
    @__Check_resize
    def pop(self, k=None) -> object:
        ''' Retorna el elemento k de una lista y lo elimina de la misma '''
        if not k and k != 0:
            k = self.__n - 1

        if not (0 <= k < len(self)):
            raise IndexError('Índice fuera de rango')

        val = self.__A[k]

        for i in range(k, len(self) - 1):
            self.__A[i] = self.__A[i + 1]

        self.__n -= 1
        return val

    def remove(self, obj) -> None:
        ''' Elimina la primera instancia de un objeto en la lista 
        Nota: depende de la implementación de == de cada elemento '''
        idx = self.index(obj)
        self.pop(idx)


    def extend(self, l:ListaDinamica) -> None:
        ''' Agrega elementos al final de la lista '''
        self += l
        

    def reverse(self) -> None:
        ''' Invierte los elementos de la lista '''
        for i in range(len(self) // 2):
            self.__A[i], self.__A[self.__n -i -1] = \
                self.__A[self.__n -i -1], self.__A[i] 


    
    def sort(self) -> None:
        ''' Ordena los elementos de la lista en forma ascendente (InsertionSort)'''
        for i in range(1, self.__n):
            cur = self.__A[i]
            j = i 

            while j > 0 and self.__A[j - 1] > cur:
                self.__A[j] = self.__A[j - 1]
                j -= 1
        
            self.__A[j] = cur

    def __resize(self, c) -> None:
        ''' Modifica el tamaño de la lista interna '''
        B = self.__init_arr(c)

        for k in range(self.__n):
            B[k] = self.__A[k]

        self.__A = B
        self.__c = c

    def __init_arr(self, capacidad):
        ''' Regresa un nuevo arreglo con capacidad determinada '''
        return (capacidad * ctypes.py_object)()     # Magia

if __name__ == '__main__':
    ''' Pruebas de la clase '''
    ld = ListaDinamica()

    # Agregar elementos a la lista
    ld.append(1)
    ld.append(2)
    ld.append(3)
    ld.append(4)
    ld.append(5)

    # Imprimir la lis
    print(ld)

    #Probando el metodo de len
    print('Len = ', len(ld))

    # Probando el metodo de pop
    ld.pop()
    print('Después de Pop():\n', ld)

    # Probando el metodo de insert
    ld.insert(1, 10)
    print('Después de insert(2, 10):\n', ld)

    # Probando el metodo de remove
    ld.remove(3)
    print('Después de remove(3):\n', ld)

    # Probando el metodo de reverse
    ld.reverse()
    print('Después de reverse():\n', ld)

    # Probando el metodo de sort
    ld.sort()
    print('Después de sort():\n', ld)
    
    # Probando el método __getitem__
    elemento = ld[1]
    print("Elemento en la posición 1:\n", elemento)
    
    # Probando el método __contains__
    print("¿El elemento 10 está en la lista?\n", 10 in ld)
    
    # Probando el método __eq__
    otra_lista = ListaDinamica()
    otra_lista.append(5)
    otra_lista.append(15)
    print("¿Las listas son iguales?\n", ld == otra_lista)
    
    # Probando el método __ne__
    print("¿Las listas son diferentes?\n", ld != otra_lista)
    
    # Probando el método __delitem__
    del ld[0]
    print("Lista después de eliminar el primer elemento:\n", ld)
    
    # Probando el método __add__
    nueva_lista = ld + otra_lista
    print("Lista después de concatenarla con otra lista:\n", nueva_lista)
    
    # Probando el método __iadd__
    ld += otra_lista
    print("Lista después de concatenarla con otra lista (in-place):\n", ld)
    
    # Probando el método count
    print("Número de veces que aparece el elemento 5:\n", ld.count(5))
    
    # Probando el método index
    print("Índice de la primera aparición del elemento 15:\n", ld.index(15))