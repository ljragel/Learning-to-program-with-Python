

user_input = input("Dime el número que deseas agregar a la lista: ")

user_number_list = []

while user_input != "FIN":
    user_number_list.append(user_input)
    print("¡Número añadido correctamente!")
    user_input = input("Introduce un nuevo número para añadirlo: ").upper()

list_longitude = len(user_number_list)
initial_index = 0

print(list_longitude)


