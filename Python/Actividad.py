lista = [2, 1, 3, 4, 5, 3, 9]

for i in range(len(lista)):       
        for j in range(len(lista)-i-1): 
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

print(lista)