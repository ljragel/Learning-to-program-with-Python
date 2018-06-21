


number_to_guess = int(input("Introduce el número a adivinar entre el 1 y el 10:"))

while number_to_guess <=10 and number_to_guess >=0:
    first_attempt = int(input("Dime un número a ver si lo adivinas:"))
    if first_attempt == number_to_guess:
        print("¡Lo has acertado!")

    else:
        print("Has fallado, prueba otra vez:")

print("El número debe ser menor o igual que 10 y mayor o igual que cero")

