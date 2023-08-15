edad = int(input("Ingresa tu edad: "))

if edad < 3:
    print("Aún no está en edad de ir a la escuela.")
elif edad >= 3 and edad <= 5:
    print("Kinder")
elif edad >= 6 and edad <= 11:
    print("Primaria")
elif edad >= 12 and edad <= 14:
    print("Secundaria")
elif edad >= 15 and edad <= 17:
    print("Preparatoria")
else:
    print("Profesional")