## crear una lista de notas de 5 estudiantes ##
notas = [8.5, 7.0, 9.2, 6.8, 7.5]

## recorrer la lista. mostrar quien aprobo y quien no aprobo ##
for i in range(len(notas)):
    if notas[i] >= 7.0:
        print("El estudiante", i + 1, "aprobo con nota:", notas[i])
    else:
        print("El estudiante", i + 1, "no aprobo con nota:", notas[i])
