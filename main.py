import openpyxl # type: ignore


estudiantes = {}


for i in range(3):
    nombre = input(f"Ingresa el nombre del estudiante {i + 1}: ")
    nota = float(input(f"Ingresa la nota de {nombre}: "))
    estudiantes[nombre] = nota


libro = openpyxl.Workbook()
hoja = libro.active


hoja["A1"] = "Aprobados (>=60)"


fila = 2
for nombre, nota in estudiantes.items():
    if nota >= 60:
        hoja[f"A{fila}"] = nombre  #
        fila += 1


libro.save("ejercicio2.xlsx")
print("¡Ejercicio 2 guardado en ejercicio2.xlsx!")
