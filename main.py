# asignaturas = ['Algoritmos', 'Diseño Web', 'Soporte de TI', 'Desarrollo Personal']
asignaturas = []
desaprobadas = []
notas = []

while True:
    asignatura = str(input("Ingrese el nombre de la asignatura: "))
    seguir = str(input("Ingrese (S-s) para continuar y otra letra para terminar de ingresar asignaturas: "))

    asignaturas.append(asignatura)

    if seguir != 'S' and seguir != 's':
        break

copiaAsignaturas = asignaturas

for i in range(len(copiaAsignaturas)):
    nota = int(input("Ingrese la nota para {}".format(copiaAsignaturas[i])))
    notas.append(nota)

for i in range(len(notas)):
    if (notas[i] < 11):
        desaprobadas.append(asignaturas[i])

print("Asignaturas desaprobadas: ")
for i in range(len(desaprobadas)):
    print("===> {}".format(desaprobadas[i]))