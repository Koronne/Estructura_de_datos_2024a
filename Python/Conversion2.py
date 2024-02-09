from Nodo2 import Nodo

e = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    head = Nodo()
    curr = head
    i = 0
    while i < len(e):
        curr.val = e[i]
        curr.next = Nodo()
        curr.next.prev = curr  # El prev que definimos en clases
    
        curr = curr.next
        i += 1

    # Aquí imprimo los datos de la lista e
    temp = head
    while temp:
        print(temp)
        temp = temp.next

    # Aquí imprimo los datos de la lista e en reversa
temp = head
while temp.next:
    temp = temp.next

while temp:
        print(temp)
        temp = temp.prev