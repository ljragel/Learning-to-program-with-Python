

user_solicitude = int(input("¿De qué número quieres la tabla de multiplicar?:"))

for multiple in range(1, 11):

    resultado = user_solicitude * multiple
    if resultado % 2 ==0:
        print("{} x {} = {}".format(user_solicitude, multiple, (user_solicitude * multiple)))