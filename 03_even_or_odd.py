# SOLID (S): Principio de Responsabilidad Única. La función solo evalúa la paridad.
# CLEAN CODE: Nombre con prefijo 'is_' que indica claramente un retorno booleano.

def is_even(number: int) -> bool:
    return number % 2 == 0

print(is_even(3))
print(is_even(4))