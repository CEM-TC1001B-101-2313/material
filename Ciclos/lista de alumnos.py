
alumnos = ["Pedro", "Dereck", "Benito", "Doki", "Juan"]

nombre = input("Ingresa el nombre del alumno a buscar: ")

encontrado = False
for i in alumnos:
    if i == nombre:
        encontrado = True

if encontrado:
    print("Alumno encontrado.")
else:
    print("Alumno no encontrado.")
