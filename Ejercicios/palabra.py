# Este programa pide a un usuario que escriba una palabra, la cual luego se mostrara en pantalla
# tambien le pide la cantidad de veces que esta se va a repetir, luego que ingresa el valor numerico
# deberia aparecer un lista con la palabra la cual se repite de forma vertical

# el codigo esta dañado, en el momento no funciona, la idea es que lo arregle y anexo a esto le cree
# un consecutivo numero para poder ver la cantidad de veces que se repitio sin necesidad de contarlas
# en la pantalla

# NOTA: no olvide que debe descargarlo a su local, hacer los cambios y luego volverlos a subir
"""
frase = input("Que palabras quieres mostrar en pantalla")
# le pedimos al usaurio que nos indique las veces que quiere que las muestre
num1 = int(input("Cuantas veces quieres imprimir tu palabra en pantalla"))

# en el ciclo le indicamos que hagala repeticion desde 0 hasta el valoringresado anteriormente
for x in range(0, num1):

    # asi sacamos la palabra que el usuario ingreso al inicio
    print(frase)
"""
# le pedimos al usaurio que nos indique las veces que quiere que las muestre y que palabra quiere repetir
palabra = input("Que palabra quieres mostras?: \n")
repeticion = int(input("cuantas veces quieres repetir esta palabra?: \n"))

contador = 0

for i in range(0, repeticion):
    contador = contador + 1
    print(f"La palabra: {palabra}, se repitio: {contador}")