Nombre = ["Juan", "María", "Pedro", "Laura", "Carlos", "Ana"]
Edad = [25, 30, 22, 28, 35, 27]
Ciudad = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Bilbao"]
Altura = [1.75, 1.80, 1.65, 1.70, 1.60, 1.85]


for i in range(len(Nombre)):
    print("Nombre:", Nombre[i])
    print("Edad:", Edad[i])
    print("Ciudad:", Ciudad[i])
    print("Altura:", Altura[i])
    print("--------------------")

    print(type(Nombre[i]), type(Edad[i]), type(Ciudad[i]), type(Altura[i]))
    