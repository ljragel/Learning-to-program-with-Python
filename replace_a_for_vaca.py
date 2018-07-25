"""
Crear un programa que cambie todas las ‘A’ o ‘a’ por la string ‘VACA’ de una string introducida por el usuario.
"""

user_sentence = input("Introduce una frase para ejecutar el programa: ")

print("Su frase final es: {}".format(user_sentence.replace("a", "VACA")))