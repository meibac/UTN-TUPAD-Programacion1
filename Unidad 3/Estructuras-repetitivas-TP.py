#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for num in range(100+1):
    print (num)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene. 

num = int(input("Ingrese un numero: "))

digitos = 0
num
if num == 0:
    digitos = 1
else:
    while num > 0:
        num = num // 10
        digitos = digitos + 1
print ( "La catidad de digitos es:", digitos)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
suma = 0
#para que se ejecute igual si num1 es mayor a num2
if num1 > num2:
    mayor = num1
    num1 = num2 
    num2 = mayor
for i in range (num1 + 1, num2):
        suma = suma + i 
print ("El resultado de la suma de  los 2 numeros ingresado es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.

suma = 0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    suma = suma + num
print("Suma total:", suma)


     
