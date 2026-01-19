# Nombres Significativos (Meaningful Names)
# Tipado de Datos (Type Hinting)
# Responsabilidad Única (Single Responsibility)

def sumar(numero_a, numero_b):
    return numero_a + numero_b

n1 = int(input('Introduzca el 1er número: '))
n2 = int(input('Introduzca el 2do número: '))

resultado = sumar(n1, n2)

print(f'La suma es: {resultado}')