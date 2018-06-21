

pokemon_elegido = input("¿Contra qué pokemon quieres combatir? (Bulbasaur/ Charmander / Squirtle):")

# Características pikachu
vida_pikachu = 100
chispazo = 8
bola_voltio = 10

if pokemon_elegido == "Bulbasaur":
    vida_enemigo = 100
    daño_enemigo = 6
    print("La vida de {} es de {} puntos y su ataque hace {} puntos de daño".format(pokemon_elegido, vida_enemigo, daño_enemigo))

elif pokemon_elegido == "Charmander":
    vida_enemigo = 90
    daño_enemigo = 9
    print("La vida de {} es de {} puntos y su ataque hace {} puntos de daño".format(pokemon_elegido, vida_enemigo, daño_enemigo))

elif pokemon_elegido == "Squirtle":
    vida_enemigo = 60
    daño_enemigo = 12
    print("La vida de {} es de {} puntos y su ataque hace {} puntos de daño".format(pokemon_elegido, vida_enemigo, daño_enemigo))


while vida_pikachu >= 0 and vida_enemigo >=0:
    ataque_elegido = input("¿Qué ataque quieres usar contra el pokemon enemigo? (Chispazo / Bola voltio):")

    if tipo_de_ataque_elegido == "Chipazo":
        vida_enemigo -= chispazo

    elif tipo_de_ataque_elegido == "Bola voltio":
            vida_enemigo -= bola_voltio


    print("La vida de {} ahora es de {}".format(pokemon_elegido, vida_enemigo))
    print("{} te ha atacado con {} de daño".format(pokemon_elegido, daño_enemigo))
    print("La vida de pikachu ahora es de {}".format(vida_pikachu - daño_enemigo))


if vida_pikachu <=0:
    print("El combate ha terminado")
    print("Has perdido, más suerte para la próxima, ahora al hospital pokemon")
elif vida_enemigo <=0:
    print("El combate ha terminado")
    print("¡¡Has ganado!!")




