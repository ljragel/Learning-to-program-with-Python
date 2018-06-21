


print("Bienvenido a la calculadora")
operation = input("¿Qué operación desea realizar? (Suma / Resta / Multiplicación / División):")


print("Introduce acontinuación los números a operar en el orden correspondiente")
first_number = int(input("Primer número:"))
second_number = int(input("Segundo número:"))

if operation == "Suma":
    answer = first_number + second_number
    print("El resultado de la suma es: {}".format(answer))

elif operation == "Resta":
    answer = first_number - second_number
    print("El resultado de la resta es: {}".format(answer))

elif operation == "Multiplicación":
    answer = first_number * second_number
    print("El resultado de la multiplicación es: {}".format(answer))

elif operation == "División":
    answer = first_number / second_number
    print("El resultado de la división es: {}".format(answer))