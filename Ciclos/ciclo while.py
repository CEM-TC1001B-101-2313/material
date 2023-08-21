
i = 1 # Inicio
while i <= 10: # Condición de salida/paro
    print(f"El valor de i es: {i}")
    i = i + 1 # Paso - Se recomienda dejar al final del ciclo
    #i += 1

print("------------------")

texto = "hola"

# variable[posición]
# print(texto[1])

# len(texto) número de elementos dentro de texto
# print(len(texto))

# for i in texto:
i = 0
while i < len(texto):
    print(texto[i])
    i = i + 1
