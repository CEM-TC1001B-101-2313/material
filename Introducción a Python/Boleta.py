udf1 = float(input("Proporciona tu calificación de udf1: "))
udf2 = float(input("Proporciona tu calificación de udf2: "))
udf3 = float(input("Proporciona tu calificación de udf3: "))
udf4 = float(input("Proporciona tu calificación de udf4: "))
udf5 = float(input("Proporciona tu calificación de udf5: "))
udf6 = float(input("Proporciona tu calificación de udf6: "))
udf7 = float(input("Proporciona tu calificación de udf7: "))

promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6 + udf7) / 7

print("Tu promedio es:", promedio, "Estudia más.")
print("Tu promedio es: " + str(promedio) + " Estudia más.")
print("Tu promedio es: {0} Estudia más.".format(promedio))
print(f"Tu promedio es: {promedio} Estudia más.")

var = 34567472.537273
print("La variable vale: {0:,.2f}".format(var))
print(f"La variable vale: {var:,.2f}")