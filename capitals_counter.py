"""
Este programa cuenta el número de mayúsculas que hay en cualquier string dada por el usuario
"""

#Falta: No funciona porque cuenta el número de letras en general, tiene que contar solo el número de mayúsculas



user_sentence = input("Dime una frase y te diré el número de mayúsculas que hay en dicha frase: ")


n_capitals = 0

abc = ["A".upper(), "B".upper(), "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


for abc in user_sentence:
    n_capitals += 1

print("El número de mayúsculas que has utilizado es de {}".format(n_capitals))