"""
Realizar el FizzBuzz con las mismas reglas pero en el caso que el numero sea divisible entre 3 y 5, cambiar el texto por “Bazinga”.
"""

user_number_list = []

user_input = input ("Introduce un número para añadir a la lista: ").upper()

while user_input != "FIN":
    for new_number in user_input:
            user_number_list.append(new_number)
            user_input = input("Introduce un número para añadir a la lista: ").upper()

else:

    for index in range(len(user_number_list)):
        if user_number_list[index] % 3 == 0 or user_number_list[index] % 5 == 0:
            replace_data = ""
            if user_number_list[index] % 3 == 0:
                replace_data += "Fizz"

            if user_number_list[index] % 5 == 0:
                replace_data += "Buzz"

            user_number_list[index] = replace_data

    print(user_number_list)
