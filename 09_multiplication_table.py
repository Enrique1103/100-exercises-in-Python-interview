# Escribe un programa que pida un número al usuario y muestre su tabla de multiplicar del 1 al 10

def table_multp():
    number = int(input("¿De qué número quieres la tabla de multiplicacion?: "))
    for i in range(1,11):
        result = number * i
        print(f"{number} x {i} = {result}")

table_multp()

        
