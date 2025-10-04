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
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

num_correcto = 6
acum = 0
num = int(input("Ingrese un numero: "))
while num != num_correcto:
  acum = acum + 1
  num = int(input("Ingrese otro numero: "))
print("Correcto. La cantidad de intentos fueron: ", acum)

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

for num in range(100,0, -2):

    print(num) 

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero: "))
suma = 0 
for i in range (0,num):
    suma = suma + i
print ("La suma de los numeros comprendidos entre el 0 y tu numero es: ",suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).


positivos = 0
negativos = 0
pares = 0
impares = 0
for i in range(100):
    print("Ingrese un numero: ")
    num = int(input())
    if num > 0:
        positivos = positivos + 1 
    if num < 0:
        negativos = negativos + 1
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print ("La cantidad de numeros positivos: ", positivos)
print("Negativos: ",negativos)
print ("Pares", pares)
print ( "Impares", impares)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

cont = 0 
acum = 0
for i in range(100):
   print("Ingrese un numero: ")
   num = int(input())
   cont = cont + 1
   acum = acum + num


print ("La media de los valores ingresados es: ",acum//cont)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un numero: "))
inv = 0

while num != 0:
    digito = num % 10
    inv = inv * 10 + digito 
    num = num // 10
print("El numero invertido es: ",inv)

    



     
