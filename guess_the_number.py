

number_to_guess = 5

user_number_one = int(input("Dime un número del 1 al 10:"))

0 < user_number_one <10

if 0 < user_number_one < 10:

    if user_number_one == number_to_guess:
        print("¡Lo has adivinado!")

    else:
        print("¡No lo has adivinado! Prueba otra vez")
        user_number_one = int(input("Dime un número del 1 al 10:"))

        if user_number_one == number_to_guess:
            print("¡Lo has adivinado!")

        else:
            print("¡No lo has adivinado! Prueba otra vez")
            user_number_one = int(input("Dime un número del 1 al 10:"))

            if user_number_one == number_to_guess:
                print("¡Lo has adivinado!")

            else:
                print("¡No lo has adivinado! Prueba otra vez")
                user_number_one = int(input("Dime un número del 1 al 10:"))

            if user_number_one == number_to_guess:
                print("¡Lo has adivinado!")

            else:
                print("¡No lo has adivinado! No tienes ni idea de cual es xD")

else:
    print("HE DICHO DEL 1 AL 10")