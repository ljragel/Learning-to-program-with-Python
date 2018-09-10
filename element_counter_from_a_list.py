"""
Este programa básicamente es una prueba para poner en práctica el principio de las listas
"""

#Falta: NO FUNCIONA



user_list = []

user_items = input("Dime un item que quieras añadir a la lista: ")

if user_items != "FIN":
    for new_item in user_list:
        user_list.append(new_item)
        print("¡Item añadido a la lista correctamente!")

else:
    print(len(user_list))



