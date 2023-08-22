
numero = int(input("Ingresa tu número: "))

print("Con for:")

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
print("Con while:")

i = 1
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i = i + 1