## Una función que convierta metros a otra unidad. Si no se especifica nada, que convierta a centímetros; pero también puede convertir a milímetros si se aclara. ##

## qué número es el primero y cuál el segundo ##

## ingresar numero 1 
numero = int(input("ingrese la distancia en metros: "))

medida = str(input("ingresa la unidad (cm/mm): "))

## metch-

match medida:
    case "cm":
        ## funcion anonima (lambda) ##
        metros_a_centimetros = lambda numero: numero * 100
        print(metros_a_centimetros(numero))
        ## funcion nombrada (def) ##
        def metros_a_centimetros(numero):
            return numero * 100
        print(metros_a_centimetros(numero))
    case "mm":
        ## funcion anonima (lambda) ##
        metros_a_milimetros = lambda numero: numero * 1000
        print(metros_a_milimetros(numero))
        ## funcion nombrada (def) ##
        def metros_a_milimetros(numero):
            return numero * 1000
        print(metros_a_milimetros(numero))
    case _:
        ## funcion anonima (lambda) ##
        metros_a_centimetros = lambda numero: numero * 100
        print(metros_a_centimetros(numero))
        ## funcion nombrada (def) ##
        def metros_a_centimetros(numero):
            return numero * 100
        print(metros_a_centimetros(numero))

