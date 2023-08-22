
cuenta = 0
precio = 0
while precio >= 0:
    cuenta = cuenta + precio
    precio = float(input("Ingresa el precio del producto: "))
print(f"El total a pagar es: ${cuenta:,.2f}")