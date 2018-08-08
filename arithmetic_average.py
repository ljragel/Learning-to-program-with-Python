"""
Este programa calcula la media aricmética de varios números introducidos por el usuario
"""

#Falta: Hacer que la calculadora haga la media con números decimales o de coma flotante (8.9)



number_list = []
loop_finalized = False

while loop_finalized == False:
    number = float(input("Introduce los números con los que deseas operar la media aricmética: ").upper())

    if number:
        number_list.append((number))
        print("¡El número ha sido añadido correctamente!")
        print('Recuerda que para finalizar la lista de números debes escribir "fin"')


    else:
        loop_finalized = True

list_len = len(number_list)

total = 0
for i in number_list:
    total += i

result = total / list_len

print("La media aricmética  de {} es {}".format(number_list, result))