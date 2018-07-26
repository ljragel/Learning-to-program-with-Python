"""
Crear un programa que le repita al usuario todo lo que dice pero con todas las vocales cambiadas por i
"""


user_sentence = input("Introduce una frase para ejecutar el programa: ")

print("Su frase final es: {}".format(user_sentence.replace("a", "i").replace("e", "i").replace("o", "i").replace("u", "i")))