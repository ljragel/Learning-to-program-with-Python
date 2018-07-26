

user_sentence = input("Escriba una frase: ")

vocal_number = ["a", "e", "i", "o", "u"]
all = ["b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "x", "y", "z"]

n_vocals = 0
n_consonants = 0
others = 0



for letter in user_sentence:
    if letter in vocal_number:
        n_vocals += 1

    else:
        n_consonants += 1

for all in user_sentence:
    others += 1


print("El número total de letras es {}".format(others))
print("El número de vocales es {}".format(n_vocals))
print("El número de consonantes es {}".format(n_consonants))

