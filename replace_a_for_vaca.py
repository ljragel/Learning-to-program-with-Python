"""
Crear un programa que cambie todas las ‘A’ o ‘a’ por la string ‘VACA’ de una string introducida por el usuario.
"""

user_sentence = input("Introduce una frase para ejecutar el programa: ")


final_sentence_1 = user_sentence.replace("A", "VACA")

print("Su frase final es: {}".format(final_sentence_1.replace("a", "VACA")))