


user_solicitude = int(input("¿De qué número quieres la tabla de multiplicar?:"))
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for multiple in numbers:

    resultado = user_solicitude * multiple

    print("{} x {} = {}".format(user_solicitude, multiple, (user_solicitude * multiple)))