
"""
Dada una lista mixta de enteros y strings, devolver dos listas, una con todos los enteros y otra con todas las strings.
"""

user_list = []

user_input = (input("Dime un nuevo item para añadirlo en la lista (Introduce  'Fin' para finalizar la lista): ".upper()))

while user_input != "FIN":
    user_list.append(user_input)
    print("Item añadido")
    user_input = (input("Dime un nuevo item para añadirlo en la lista: "))



total_items = len(user_list)

for new_item in user_list:
    if new_item == str: