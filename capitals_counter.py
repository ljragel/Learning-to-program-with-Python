

user_sentence = input("Dime una frase y te diré el número de mayúsculas que hay en dicha frase: ")


n_capitals = 0

abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


for abc in user_sentence:
    n_capitals += 1

print("El número de mayúsculas que has utilizado es de {}".format(n_capitals))