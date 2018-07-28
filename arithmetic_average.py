"""
Este programa calcula la media aricmética de varios números introducidos por el usuario
"""

number_list = []
loop_finalized = False

while loop_finalized == False:
    number = input("Que numero quieres introducir: ")
    if not number == "fin":
        number_list.append(int(number))
    else:
        loop_finalized = True

list_len = len(number_list)

total = 0
for i in number_list:
    total += i

result = total / list_len

print("La media de {} es {}".format(number_list, result))