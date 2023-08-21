udfs = int(input("¿Cuántas udfs cursaste en el semestre?: "))

promedio = 0
for i in range(1, udfs+1):
    udf = float(input(f"Proporciona tu calificación de udf{i}: "))
    promedio = promedio + udf
    #promedio += udf
promedio = promedio / udfs
#promedio /= udfs

print(f"Tu promedio es: {promedio:,.0f}.")

if promedio > 90:
    print("Fue un semestre excelente.")
elif promedio >= 80:
    print("Fue un buen semestre.")
else:
    print("Debes estudiar más.")
