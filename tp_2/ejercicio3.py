##  Una función que calcule el precio final de un producto aplicando un IVA, que por defecto sea del 21%. ##

## ingresar el valor del producto

producto = int(input("ingrese el valor del producto: "))   

## funcion anonima (lambda) ##

precio_final = lambda producto, iva = 0.21: producto + (producto * iva)
print(precio_final(producto))

## funcion nombrada (def) ##

def precio_final(producto, iva = 0.21):
    return producto + (producto * iva)
print(precio_final(producto))

