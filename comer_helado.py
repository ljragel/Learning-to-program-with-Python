

me_apetece_helado_input = input("¿Te apetece un helado? (Si/No): ").upper()

if me_apetece_helado_input == "SI":
    me_apetece_helado = True

else:
    me_apetece_helado = False
    print("Pues no te comas el helado")


esta_el_señor_de_los_helados_input = input("¿Está el señor de los helados? (Si/No): ").upper()
if esta_el_señor_de_los_helados_input == "SI":
    esta_el_señor_de_los_helados = True

else:
    esta_el_señor_de_los_helados = False
    print("Entonces no te puedes comer el helado porque no lo puedes comprar")

tienes_dinero_input = input("¿Tienes dinero para comprar el helado? (Si/No): ").upper()

if tienes_dinero_input == "SI":
    tienes_dinero = True

else:
    tienes_dinero = False
    print("Quizás estás con tu tía")


esta_tu_tia_input = input("¿Está tu tía? (Si/No): ").upper()
if esta_tu_tia_input == "SI":
    tienes_dinero = True

else:
    tienes_dinero = False
    print("Entonces si que no puedes comerte el helado porque no lo puedes pagar")


me_apetece_helado = me_apetece_helado_input == "SI"
esta_el_señor_de_los_helados = esta_el_señor_de_los_helados_input == "SI"
tienes_dinero = tienes_dinero_input == "SI" or esta_tu_tia_input == "SI"

if me_apetece_helado and esta_el_señor_de_los_helados and tienes_dinero:
    print("Pues cómete un helado")

else:
    print("No puedes comertelo")