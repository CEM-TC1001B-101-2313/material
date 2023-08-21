# Ciclo for

# range(final)
# Genera una secuencia de números que inician en 0, avanzan
# de 1 en 1 y llegan hasta antes de final
for i in range(5):
    print(f"El valor de i es: {i}")

print("-------------------")

# range(inicio, final)
# Genera una secuencia de números que inician en inicio, avanzan
# de 1 en 1 y llegan hasta antes de final
for i in range(3, 8):
    print(f"El valor de i es: {i}")

print("-------------------")

# range(inicio, final, paso)
# Genera una secuencia de números que inician en inicio, avanzan
# de paso en paso y llegan hasta antes de final
for i in range(3,12,2):
    print(f"El valor de i es: {i}")

print("-------------------")

for i in range(5,10,-2):
    print(f"El valor de i es: {i}")
    
print("-------------------")

texto = "Hola mundo"

for i in texto:
    print(f"El valor de i es: {i}")
    
print("-------------------")


lista = [1,2,4,True,"Hola",["Otra", "Lista"]]

for i in lista:
    print(f"El valor de i es: {i}")