"""
Crea un programa que cuente el número de veces que aparece una palabra en una string
"""

#


counter = dict()

print("Contador de palabras en una frase")
print("------------------------------------")
user_string = input("Frase: ")


for new_word in user_string.split(" "):
    new_word_times = 0
    word = new_word
    new_word_times += 1
    counter[new_word] = new_word_times


print(counter)
