
""""
Escribe un programa que encuentre el numero más grande entre 3 numeros
"""
#Da "error" (function biggest_number at 0x0159B618), no funciona del todo

input_numbers = input("Dame 3 números para poder realizar mi función (Introdúcelos separados por comas y espacio): ")



def biggest_number(input_numbers):
    list = []
    current_index = len(input_numbers) - 1
    while current_index <= 4:
        first_number = list.append(input_numbers[0])
        second_number = list.append(input_numbers[1])
        third_number = list.append(input_numbers[2])

    biggest_number = 0
    for item in list:
        if biggest_number < item:
            biggest_number = item

    return input_numbers

print(biggest_number)



