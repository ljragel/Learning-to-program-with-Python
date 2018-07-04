

shopping_list = []
user_input = input("Introduce el elemento que deseas añadir a la lista de la compra (Escribe fin si deseas finalizar la lista):").upper()



while user_input != "fin".upper():
    shopping_list.append(user_input)
    user_input = input("Introduce el elemento que deseas añadir a la lista de la compra (Escribe fin si deseas finalizar la lista):").upper()


longitude_list = len(shopping_list)
initial_index = 0

for user_input in shopping_list:
    print("Debes comprar {}".format(user_input))