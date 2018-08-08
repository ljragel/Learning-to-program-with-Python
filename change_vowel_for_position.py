"""
Crear un programa que cambia las vocales por su numero de aparición. Por ejemplo la string “aurora boreal” se convertiría en “12r3r4 b5r67l
"""

#Falta: NO FUNCIONA, ¿Forma para replace justo en el lugar donde vaya? user_sentence[X]



user_sentence = input("Introduce una frase para ejecutar el programa: ")

vowel = ("a", "e", "i", "o", "u")

for vowel in user_sentence:
    print(user_sentence.replace(user_sentence[2]))