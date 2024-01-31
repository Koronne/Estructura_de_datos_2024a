#Aqui definimos la funcion que e colocado como fib por Fibonacci con su argumento n de forma recursiva
def fib(n):
    #Aqui verifico si el valor de n es mayor a 1, por ejemplo si los digitos 0 y 1, como 0 es menor que 1 se regresa y como 1 es igual 1, se regresa igual
    #y se coloca, ya que la formula de Fibonacci es asi
    if n > 1:
        #La formula
        return fib(n - 1) + fib(n - 2)
    return n

#Aqui coloco una variante, para que usted o yo ingrese un numero por la funcion input
x = int(input("Ingresa un numero: "))

#Creo una lista para el acomodo de los numeros que deseamos anteriormente con el input
t=[fib(i) for i in range(x)]
#Aqui lo imprimo
print(t)