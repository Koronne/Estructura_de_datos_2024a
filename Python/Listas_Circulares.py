from Nodo3 import Node_Liga_Circular

e = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    head = Node_Liga_Circular()
    curr = head
    first_node = head  # Hago una referencia para el primer nodo

    for i in e:
        curr.val = i
        curr.next = Node_Liga_Circular()
        curr = curr.next
         # Conecta el último nodo con el primer nodo para formar un ciclo
        curr.next = first_node

    # Imprime los valores de la lista ligada circular
    Nodo_Nuevo = head
    for _ in range(len(e)):
        print(Nodo_Nuevo)
        Nodo_Nuevo = Nodo_Nuevo.next