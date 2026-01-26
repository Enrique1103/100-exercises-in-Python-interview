#Escribe una función que reciba un número entero positivo y devuelva 
# su factorial (el producto de todos los números desde 1 hasta ese número).

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial_iterativo(5))