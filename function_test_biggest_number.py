"""
Escribe una función que encuentre el numero más grande entre 3 numeros.
"""

def biggest_number (primero, segundo, tercero):

    primero = len(1, total_numbers_list)

    if len(1, total_numbers_list) >= 0:
        biggest_number = len(1, total_numbers_list)

    elif len(2, total_numbers_list) > len(1, total_numbers_list):
        biggest_number = len(2, total_numbers_list)

    elif len(3, total_numbers_list) > len(1, total_numbers_list) and len(2, total_numbers_list):
        biggest_number = len(3, total_numbers_list)

    return biggest_number



total_numbers_list = []

while len(total_numbers_list) < 3:
    user_input = input("Dime uno de los 3 números para añadirlo a la lista: ")
    total_numbers_list.append(user_input)

print(biggest_number(total_numbers_list))



