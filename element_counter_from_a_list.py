

user_list = []

user_items = input("Dime un item que quieras añadir a la lista: ")

while user_items != "FIN":
    for new_item in user_list:
        user_list.append(user_items)

print(user_list)



