"""
bueno entonces cree un repositorio en github y me lo comparte, me encuentra como (@legarrod) y alli cree un programa en python sencillo, un programa que pida un numero incial y un numero final, luego que la salida sea una secuencia de numeros que aumente de 2 en 2. Por ejemplo:

Digite numero inicial: 2
Digite numero final: 10
Resultado: 2
4
6
8
10
"""
#Se ingresa el numero inicial y el numero final


def ciclo_while(numero_inicial, numero_final): #se crea el metodo ciclo_while 
    while numero_inicial < numero_final: #se crea la operacion de la suma en while
        numero_inicial = numero_inicial + 2
        print(numero_inicial)

def ciclo_for(numero_inicial,numero_final): #se crea el metodo ciclo_for
    for i in range(numero_inicial, numero_final): #se crea la operacion en for
        numero_inicial= numero_inicial + 2
        print(numero_inicial)

#Ingreso de los valores
numero_inicial = int(input("ingrese el numero inicial: \n"))
numero_final = int(input("ingrese el numero final: \n"))
#llamados a los metodos
ciclo_while(numero_inicial,numero_final)
ciclo_for(numero_inicial,numero_final)