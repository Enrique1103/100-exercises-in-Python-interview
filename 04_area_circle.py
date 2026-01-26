# CLEAN CODE: Nombre descriptivo en formato 'verbo_sustantivo' (Acción clara).
# SOLID (S): Principio de Responsabilidad Única. La función solo calcula, no imprime.

from math import pi

def calulater_circle_area(radius: float) -> float:
    return pi * radius ** 2

area = calulater_circle_area(2)
print(f'The area of a circle is: {area:.2f}')
