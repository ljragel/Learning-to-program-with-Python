""""
Crear un programa que guarde e imprima varias listas con todos los números que estén dentro de una lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.

Ejemplo:

input = [1, 10, 70, 30, 50, 55]

multiplos_dos = [10, 70, 30, 50]
multiplos_tres = [30]
multiplos_cinco = [10, 70, 30, 60, 55]
multiplos_siete = [70]
"""

user_number_list = []
two_list = []
three_list = []
five_lits = []
seven_list = []




user_input = input("Introduce un nuevo número para añadirlo: ").upper()

while user_input != "FIN":
    user_number_list.append(user_input)
    print("¡Número añadido correctamente!")
    user_input = input("Introduce un nuevo número para añadirlo: ").upper()

    for index in range(len(user_number_list)):
        if user_number_list[index] % 2 == 0:
            two_list.append(user_number_list[index], end="")

print("Los números múltiplos de 2 son: {}".format(two_list))
print("Los números múltiplos de 3 son: {}".format(three_list))
print("Los números múltiplos de 5 son: {}".format(five_lits))
print("Los números múltiplos de 7 son: {}".format(seven_list))
