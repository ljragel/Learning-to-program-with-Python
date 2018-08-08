"""
Este programa es solo una prueba sin inpuut de usuario para poner en práctica el concepto while
"""

first_number = 10

print("El número {} es par".format(first_number))

while first_number > 0:
    first_number = first_number - 1

    if first_number % 2 == 0:
        print("El número {} es par".format(first_number))

    else:
        print("El número {} es impar".format(first_number))



