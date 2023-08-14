salario_bruto = float(input("Indica tu salario: "))
isr = salario_bruto * 0.2136
salario_neto = salario_bruto - isr
print(f"El ISR que se te descontó es: ${isr:,.2f}")
print(f"Tu salario neto es de: ${salario_neto:,.2f}")