
""""
Escribe un programa que encuentre el numero más grande entre 3 numeros
"""

input_numbers = input("Dame 3 números para poder realizar mi función (Introdúcelos separados por comas y espacio): ")

def biggest_number():
    current_index = 0
    biggest_number = 0
    while current_index <= 4:
        if input_numbers[0] > 0:
            biggest_number = input_numbers[0]
            current_index += 1


final = biggest_number(input_numbers)

print(final)



