## Una función que reste dos números, pero al usarla se debe indicar explícitamente
## qué número es el primero y cuál el segundo ##

## ingresar numero 1  y 2
numero1 = int(input("ingrese el primer numero: "))

numero2 = int(input("ingrese el segundo numero: "))

## funcion anonima (lambda) ##

resta2 = lambda numero1, numero2: numero1 - numero2
print(resta2(numero1,numero2))

## funcion nombrada (def) ##
def resta(numero1,numero2):
    return numero1 - numero2
resultado = resta(numero1,numero2)
print(resultado)
