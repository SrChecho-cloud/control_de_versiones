## Una función que reciba dos números en el orden que se pasan y devuelva la suma. ##

## funcion anonima (lambda) ##

suma2 = lambda x, y=1: x + y
print(suma2(3,5))

## funcion nombrada (def) ##
def suma(a,b):
    return a + b
resultado = suma(3,5)
print(resultado)
