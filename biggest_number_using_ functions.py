
""""
Escribe un programa que encuentre el numero más grande entre 3 numeros
"""

#Funciona pero no siempre correctamente a veces devuelve realmente el número mayor pero otras no (tiene un problema con el número 10) PD: Estaría bien utilizar una función propia en vez de max()


print("¡Introduce 3 números para calcular el mayor de ellos!")

numbers_list = []
def security_answer(question):
    if question.isdigit():
        numbers_list.append(question)
        print("¡Número añadido correctamente!")


question = security_answer(input("Inserte el primer número para añadirlo a la lista: "))

question = security_answer(input("Inserte el segundo número para añadirlo a la lista: "))

question = security_answer(input("Inserte el último número para añadirlo a la lista: "))


print("El número más grande de los tres es {}".format(max(numbers_list)))




