"""
Crear un programa que encuentre el numero más grande de una lista (sin usar la función max).
"""

numbers_user_list = []

user_numbers = ""


while len(numbers_user_list) < 10:
    while not user_numbers.isdigit():
        user_numbers = input("Dime un número: ")
    numbers_user_list.append(int(user_numbers))
    user_numbers = ""
    print("¡Número añadido! ")


smallest_number = numbers_user_list[0]


for number in numbers_user_list:
    if number > smallest_number:
        smallest_number = number

print("El número más grande es {}".format(smallest_number))