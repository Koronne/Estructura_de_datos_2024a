from Nodo import Nodo

e = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    head = Nodo()
    curr = head
    i = 0
    while i < len(e):
        curr.val = e[i]
        if i < len(e):
            curr.next = Nodo()
            curr = curr.next
        i += 1

    # Aqui imprimo los datos de la lista e
    temp = head
    while temp:
        print(temp)
        temp = temp.next