"""
Escribe una función que reciba una lista de números y devuelva otra pero conteniendo solo los números pares.
"""
#


user_input = input("Introduce un número para añadirlo a lista y poder ejecutar el programa (FIN para finalizar la lista): ").upper()
numbers_list = []


while user_input != "FIN":
    for new_item in user_input:
        numbers_list.append(new_item)
        print("¡Número añadido correctamente!")
        user_input = input("Introduce un número para añadirlo a lista y poder ejecutar el programa (FIN para finalizar la lista): ").upper()


        def pair_numbers(numbers_list):
            for number in numbers_list:
                if number % 2 == 0:
                    print("Los números {} son pares".format(number))

while not user_input != "FIN":

    print(pair_numbers(numbers_list))