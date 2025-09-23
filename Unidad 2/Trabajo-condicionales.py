#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Igrese su edad: "))
if edad >= 18:
   print ("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”.    
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else :
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.    

num = int(input("Ingrese un numero: "))
if num % 2 == 0: 
    print("Es numero par")
else :
    print("Porfavor ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.    

edad = int(input("Ingrese su edad: "))
if edad <= 12:
    print("Es un niño/a")
elif edad >= 12 and edad <= 18:
    print("Es un adolescente")
elif edad >=18 and edad <= 30:
    print("Es adulto/a joven")
else : 
    print("Es mayor")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string. 

contraseña = input("Ingrese una contraseña (Debe tener de 8 a 14 caracteres): ")
contraseña = len(contraseña)
if contraseña >= 8 and contraseña <=14:
    print("Ha ingresado una contraseña correcta.")
else :
    print("Ingrese una contraseña de 8 a 14 caracteres.")

#6) escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
#Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
#mediana es mayor que la moda. 
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
#la mediana es menor que la moda. 
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.

import random 
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print ("Sesgo positivo.")
elif media < mediana and mediana < moda:
    print ("Sesgo negativo.")
elif media == mediana and mediana == moda:
    print ("Sin sesgo.")

print(f"La moda es: {moda},La mediana es: {mediana},Y la media es: {media}")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla. 

palabra = str(input("Ingrese una palabra "))
vocales = ("a","e","i","o","u")
ultima_letra = palabra[-1]
if ultima_letra in vocales:
    print (f"{palabra}!")
else :
    print (palabra)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = str(input("Ingrese su nombre: "))
opcion = int(input("Elija 1, si quiere su nombre en mayusculas. 2, si lo quiere en minusculas. 3, si quiere su nombre con la primera letra mayuscula." ))
mayusculas = nombre.upper()
minusculas = nombre.lower()
primera_letra = nombre.title()


if opcion == 1:
    print(mayusculas)
elif opcion == 2:
    print(minusculas)
elif opcion == 3: 
    print(primera_letra)
else:
    print("Numero invalido.")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = int(input("Ingrese la magnitud del terremoto para calcularlo en su escala de Richter: "))

if magnitud < 3:
    print ("Muy leve, (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve, (Ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (Sentido por personas pero generalmente no causa daño.)")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte, (Puede causar daños en estructuras debiles.)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte, (Puede causar daños significativos.)")
elif magnitud >= 7:
    print("Extremo (Puede causar graves daños a escalas.)")

#10
hemisferio = str(input("Ingrese su hemisferio (Norte o Sur): ")).lower()
mes = str(input("Ingrese el mes del año en letras: "))
dia = int(input("Ingrese el dia: "))

meses = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12
}

mes_num = meses[mes]
fecha = mes_num * 100 + dia


if hemisferio == "norte":
    if fecha >= 1221 or fecha <= 320:
        print ("Usted esta en invierno")
    elif fecha >= 321 and fecha <= 620:
        print ("Usted esta primavera")
    elif fecha >= 621 and fecha <= 920:
        print ("Usted esta en verano")
    elif fecha >= 921 and fecha <= 1220:
        print ("Usted esta en otoño")

if hemisferio == "sur":
    if fecha >= 1221 or fecha <= 320:
        print("Usted está en verano")
    elif 321 <= fecha and fecha <= 620:
        print("Usted está en otoño")
    elif 621 <= fecha and fecha <= 920:
        print("Usted está en invierno")
    elif 921 <= fecha and fecha <= 1220:
        print("Usted está en primavera")
