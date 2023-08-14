
# Sin parámetros y sin valor de retorno
def suma1():
    x = float(input("Ingresa el valor de x: "))
    y = float(input("Ingresa el valor de y: "))
    resultado = x + y
    print(f"La suma de x + y es: {resultado}")

# Con parámetros y sin valor de retorno
def suma2(x, y):
    resultado = x + y
    print(f"La suma de x + y es: {resultado}")

# Con parámetros y con valor de retorno
def suma3(x, y):
    resultado = x + y
    return resultado
    print("Estoy debajo de return")
    print("Esto nunca va a aparecer")

#suma1()
#print(x)
#print(y)
#print(resultado)
# ------------------------    
#suma2(7, 5)
#a = float(input("Ingresa x: "))
#b = float(input("Ingresa y: "))
#suma2(a, b)
#print(x)
#print(y)
#print(resultado)
# ------------------------
res = 15 + suma3(4,3) / 2 - 4
print(res)
a = suma3(54, 5)