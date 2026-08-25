## ingresar dos numero ##
input1 = float(input("Ingrese el primer número: "))
input2 = float(input("Ingrese el segundo número: "))


## suma, resta, multiplicación, división y resto de la división ##
suma = input1 + input2
resta = input1 - input2
multiplicacion = input1 * input2
if input2 != 0:
    division = input1 / input2
    resto = input1 % input2

## mostrar resultados ##
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
if input2 != 0:
    print("División:", division)
    print("Resto de la división:", resto)
