"""
Escribe una función que encuentre el numero más grande entre 3 numeros.
"""

total_numbers_list = []

while len(total_numbers_list) < 3:
    user_input = input("Dime uno de los 3 números para añadirlo a la lista: ")
    total_numbers_list.append(user_input)

biggest_number = max(total_numbers_list)

print("El número más grande de los tres es el {}".format(biggest_number))




