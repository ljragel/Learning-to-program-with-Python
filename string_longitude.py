

new_data = input("Dime que una strig que quieras añadir a la lista: " ).upper()

strings_list = []

while new_data != "FIN":

    for new_string in new_data:
        strings_list.append(new_data)
    new_data = input("Dime que una strig que quieras añadir a la lista: ").upper()


print(len(strings_list))
