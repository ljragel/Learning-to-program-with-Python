"""
Crea un programa que sea capaz de guardar los nombres de tus amigos y sus años de nacimiento.
"""

#Hay algún tipo de bug qye hace que la primera persona no funcione toma el valor del dato de la segunda persona

works = False

data = dict()

while not works:

    user_action = input("¿Qué deseas hacer? [Añadir fechas [A] / Consultar fechas [C] / Salir [S]: ").upper()

    #Add
    if user_action == "A":
        print("Añadir fechas")
        print("----------------------------")
        name = input("Nombre: ")
        date = input("Fecha: ")
        data[name] = date
        print("¡Datos guardados correctamente!")

    #Search
    elif user_action == "C":
        print("Consultar fechas")
        print("----------------------------")
        question = input("¿De quién quieres saber la fecha de nacimiento?")
        print(data[name])

    #Exit
    elif user_action == "S":
        works = True
