# UTN-TUPAD-Programacion1

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")  

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla. 
nombre = input("Ingrese su nombre: ")
print (f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
print(f"Mi nombre es {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
#su perímetro. 
radio = float(input("Ingrese radio de un circulo: "))
pi = 3.14
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El area es {area} y el perimetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale. 
segundos = int(input("Ingrese una cantidad de segundos para calcular a cuantas horas equivalen: ")) 
horas = segundos / 3600
print(f"Los segundos ingresados equivales a {horas}")
#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
#multiplicar de dicho número.  
numero = int(input("Ingrese un numero: "))
t1 = numero * 1
t2 = numero * 2
t3 = numero * 3
t4 = numero * 4
t5 = numero * 5
t6 = numero * 6
t7 = numero * 7
t8 = numero * 8
t9 = numero * 9
t10 = numero * 10
print(f"La tabla de multiplicar de tu numero es: {t1} {t2} {t3} {t4} {t5} {t6} {t7} {t8} {t9} {t10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multp = numero1 * numero2
div = numero1 / numero2
print(f"Los calculos entre sus dos numeros son: suma: {suma} resta: {resta} multiplicacion: {multp} division: {div}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
alt = altura * altura
imc = peso / alt
print(f"Su indice de masa corporal es {imc}")

 #9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
celsius = int(input("Ingrese una temperatura en grados Celsius para convertirla a Fahrenheit: "))
faren = (celsius * 9)/ 5 + 32
print(faren)

# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#dichos números.
print("Ingresara 3 numeros enteros para calcular su promedio: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())
resultado = (num1 + num2 + num3)/ 3
print(f"El promedio de sus numeros es: {resultado}")

