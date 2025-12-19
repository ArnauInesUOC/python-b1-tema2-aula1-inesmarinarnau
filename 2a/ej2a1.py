"""
Enunciado:
Una tienda tiene una promoción que aplica el descuento del 10% a los productos
cuyo valor numérico sea par. Para ello se requiere implementar funciones capaces 
de sumar una lista de valores pares y retornar dicha suma.

Implementa las funciones 'sum_even_numbers_in_list_while(shopping_list)', 
'sum_even_numbers_in_list_for(shopping_list)' y
'sum_even_numbers_in_list_do_while(shopping_list)' en donde su parámetro
sea una lista de números y utilice un bucle 'WHILE', 'FOR' y 'DO WHILE', respectivamente,
para su implementación. Todas las funciones deben retornar la suma de los números pares.

Parámetros:
    shopping_list (List): lista de precios que se desea sumar

Ejemplo:
    Entrada:
    shopping_list = [10, 449, 33, 44, 188, 640]
    sum_even_numbers_in_list_while(shopping_list)
    sum_even_numbers_in_list_for(shopping_list)
    sum_even_numbers_in_list_do_while(shopping_list)

    Salida:
    En los 3 casos el resultado es 882, que es la suma de 10, 44, 188 y 640. 

"""


def sum_even_numbers_in_list_while(shopping_list):
    sum_even = 0 
    for value in shopping_list:
        if not isinstance(value, (int, float)):
            raise ValueError("Los valores en la lista deben ser enteros")
    i = 0
    while i < len(shopping_list):
        if shopping_list[i] % 2 == 0:
            sum_even += shopping_list[i]
        i += 1
    return sum_even



def sum_even_numbers_in_list_for(shopping_list):
    sum_even = 0
    for value in shopping_list:
        if not isinstance(value, (int, float)):
            raise ValueError("Los valores en la lista deben ser números")
        elif value % 2 == 0:
            sum_even += value
    return sum_even

def sum_even_numbers_in_list_do_while(shopping_list):
    sum_even = 0
    for value in shopping_list:
        if not isinstance(value, (int, float)):
            raise ValueError("Los valores en la lista deben ser enteros")
    i = 0
    while True:
        if i == len(shopping_list):
            break
        elif shopping_list[i] % 2 == 0:
            sum_even += shopping_list[i]
        i += 1
    return sum_even



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

shopping_list = [10, 449, 33, 44, 188, 640]
print(sum_even_numbers_in_list_while(shopping_list))
print(sum_even_numbers_in_list_for(shopping_list))
print(sum_even_numbers_in_list_do_while(shopping_list))
