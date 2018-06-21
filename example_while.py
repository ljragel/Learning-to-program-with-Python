first_number = 10

print(first_number)
print("Además el número es par")

while first_number > 0:
    first_number = first_number - 1

    if first_number % 2 == 0:
        print(first_number)
        print("Además el número es par")

    else:
        print(first_number)
        print("Además el número es impar")



