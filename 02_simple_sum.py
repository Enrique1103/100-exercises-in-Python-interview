# CLEAN CODE: Nombre de función como verbo (indica acción clara).
# SOLID (S): Principio de Responsabilidad Única. La función solo procesa la lógica matemática.

def add(number_a, number_b):
    return number_a + number_b

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))

result = add(n1, n2)

print(f'The sum is: {result}')