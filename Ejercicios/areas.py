import math

def cuadrado(): #Se crea la funcion para sacar el area del cuadrado
    lado = int(input("Ingrese el valor del lado (L): \n "))
    resultado = lado * lado * lado * lado
    print(f"El area de su cuadrado es: {resultado}")

def triangulo():#Se crea la funcion para sacar el area del triangulo
    base = int(input("ingrese la base (B): \n"))
    altura = int(input("ingrese la altura (H): \n"))
    resultado = base * altura / 2
    print(f"el area de su triangulo es: {resultado}")

def rectangulo():#Se crea la funcion para sacar el area del rectangulo
    base = int(input("ingrese la base (B): \n"))
    altura = int(input("ingrese la altura (H): \n"))
    resultado = base * altura
    print(f"el area de su rectangulo es: {resultado}")

def circulo():#Se crea la funcion para sacar el area del circulo
    radio = float(input("ingrese el radio (R): \n "))
    area = math.pi * radio **2
    print(f"el area de su circulo es: {circulo}")


#Se hace la pregunta de a que le quiere sacar el area
respuestas = int(input(""" 
A que quieres calcular el area:
1. Cuadrado
2. Triangulo
3. Rectangulo
4. circulo 
"""))
#Se hace la desicion para ir directamente a la funcion dependiendo la opcion
if respuestas == 1:
    cuadrado()
elif respuestas == 2:
    triangulo()
elif respuestas == 3:
    rectangulo()
elif respuestas == 4:
    circulo()
else:
    print("El dato que usted ingreso no corresponde <3")

