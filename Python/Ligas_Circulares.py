from Nodo3 import Node_Liga_Circular

e = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    head = Node_Liga_Circular()
    curr = head
    first_node = head  # Guarda una referencia al primer nodo

    for i in e:
        curr.val = i
        if i != e[-1]:
            curr.next = Node_Liga_Circular()
            curr = curr.next
        else:
            # Conecta el último nodo con el primer nodo para formar un ciclo
            curr.next = first_node
