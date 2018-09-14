"""
Crea un programa que al decirle el nombre de un color nos devuelva su traducción en inglés
"""

#


works = False

dictionary = {"Azul": "Blue", "Amarillo": "Yellow", "Verde": "Green", "Rojo": "Red", "Marrón": "Brown", "Negro": "Black", "Blanco": "White", "Gris": "Grey", "Rosa": "Pink"}

print("DICCIONARIO ESPAÑOL/INGLÉS")
print("------------------------------------")

while not works:

    color_in_spanish = input("¿Qué color quieres traducir al Inglés?: ")
    print(dictionary[color_in_spanish])