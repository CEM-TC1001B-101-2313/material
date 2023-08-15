udf1 = float(input("Proporciona tu calificación de udf1: "))
udf2 = float(input("Proporciona tu calificación de udf2: "))
udf3 = float(input("Proporciona tu calificación de udf3: "))
udf4 = float(input("Proporciona tu calificación de udf4: "))
udf5 = float(input("Proporciona tu calificación de udf5: "))
udf6 = float(input("Proporciona tu calificación de udf6: "))
udf7 = float(input("Proporciona tu calificación de udf7: "))

promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6 + udf7) / 7

print(f"Tu promedio es: {promedio:,.0f}.")

if promedio > 90:
    print("Fue un semestre excelente.")
elif promedio >= 80:
    print("Fue un buen semestre.")
else:
    print("Debes estudiar más.")
