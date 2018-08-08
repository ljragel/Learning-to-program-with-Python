"""
Este programa es un conversor de grados celcius a fahrenheit y al revés
"""



conversion_mode = int(input("¿Desea convertir celcius a fahrenheit (1) o fahrenheit a celcius (2)?:"))

if conversion_mode == int(1):
    grades_in_celcius = float(input("Introduce la unidad en grados celcius:"))
    grades_in_fahrenheit = ((9 * grades_in_celcius) / 5) + 32
    print("{} grados celcius son {} grados fahrenheit.".format(grades_in_celcius, grades_in_fahrenheit))

else:
    conversion_mode == int(2)
    grades_in_fahrenheit = float(input("Introduce la unidad en grados fahrenheit:"))
    grades_in_celcius =  (5 * (grades_in_fahrenheit - 32) / 9)
    print("{} grados celcius son {} grados fahrenheit.".format(grades_in_celcius, grades_in_fahrenheit))