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
#Esta lista es una compresion, ya que lo uso con el bucle for y ha pasado por el if, osea, por lo que entendi
#Las listas compresivas tiene que pasar por un if para que sean agregados en el for, y toda expresion de lista debe encerrarse entre corchetes.
#https://www.codigopiton.com/parentesis-corchetes-llaves-en-python/ de aqui me base mi respuesta
#Aqui lo imprimo

print(t)