# CLEAN CODE: Uso de Constantes (Screaming Snake Case) para evitar "Magic Numbers".
# Facilita el mantenimiento si las constantes de conversión necesitaran cambiar.

FREEZING_POINT_F = 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_celsius_to_fahrenheit(celcius: float) -> float:
    return (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_F

temperature_in_celsius = 20.0
result = convert_celsius_to_fahrenheit(temperature_in_celsius)

print(f"{temperature_in_celsius}°C es igual a {result}°F")