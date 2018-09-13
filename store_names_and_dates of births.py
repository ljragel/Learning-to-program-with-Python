"""
Crea un programa que sea capaz de guardar los nombres de tus amigos y sus años de nacimiento.
"""

#

works = True

data = dict()

user_action = input("¿Qué deseas hacer? [Añadir fechas [A] / Consultar fechas [C] / Salir [S]: ").upper()

while works:

#Add
if user_action == "A":
    print("Añadir fechas")
    print("----------------------------")
    name = input("Nombre: ")
    date = input("Fecha: ")
    data[name] = date
    user_action = input("¿Qué deseas hacer? [Añadir fechas [A] / Consultar fechas [C] / Salir [S]: ").upper()

#Search
elif user_action == "C":
    print("Consultar fechas")
    print("----------------------------")
    question = input("¿De quién quieres saber la fecha de nacimiento?")
    print(data[name])
    user_action = input("¿Qué deseas hacer? [Añadir fechas [A] / Consultar fechas [C] / Salir [S]: ").upper()

#Exit
elif user_action == "S":
    works = False
