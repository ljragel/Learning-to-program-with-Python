
"""
Escribe una función que dado un número y un rango (otros dos números), compruebe que ese número está entre los dos (dentro del rango).
"""
#


print("Este programa calcula si un número está dentro del rango de 0 a 100")

number_to_check = int(input("Introduce el número que deseas comprobar si está dentro del rango de 0 a 100: "))

def in_range(number_to_check):
    if number_to_check >= 0:
        if number_to_check <= 100:
            print("El número {} está dentro del rango".format(number_to_check))

        else:
            print("El número {} no está dentro del rango".format(number_to_check))


in_range(number_to_check)





