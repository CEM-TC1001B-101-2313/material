
color = input("Ingresa tu color favorito:")

match (color):
    case "amarillo":
        print("Te gustan los colores claros.")
    case "negro":
        print("Te gusta la noche.")
    case _: # caso por defecto
        print("No conozco ese color.")
