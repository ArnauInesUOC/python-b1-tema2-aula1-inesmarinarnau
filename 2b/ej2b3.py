"""
Enunciado:
Implementa una función 'triangle_area_calculate', que recibe dos parámetros,
que corresponden a la altura y la base de un triángulo que deben
ser números positivos. Dichos parámetros deben ser nombrados correctamente,
considerando las buenas prácticas de programación PEP8.
La función debe retornar el cálculo del área de un triángulo mediante los
datos introducidos, adicionalmente, el código debe tener comentarios de manera
que se vaya explicando el procedimiento.

Parámetros:
Son dos parámetros, que corresponden a la altura y la base de
un triángulo y deben ser números positivos. Se deben crear correctamente
utilizando las buenas prácticas de programación PEP8.


Ejemplo:
    Entrada:
    triangle_area_calculate(33, 45)

    Salida:
    742.5
"""


def triangle_area_calculate(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Number must be greater than 0.")
    return (base * height) / 2


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta
# el script

# Si vols provar el teu codi, descomenta les línies següents i executa
# l'scrip

print(triangle_area_calculate(33, 45))
