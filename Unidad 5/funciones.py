 #1. Crear una función llamada imprimir_hola_mundo que imprima por
 #pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 #programa principal.

def imprimir_hola_mundo():
   print("Hola mundo")

imprimir_hola_mundo()
print("")
 #2. Crear una función llamada saludar_usuario(nombre) que reciba
 #como parámetro un nombre y devuelva un saludo personalizado.
 #Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
 #principal solicitando el nombre al usuario

def saludar_usuario(nombre):
   print(f"Hola, {nombre}!")

nombre_usuario = input("Ingrese su nombre: ")
saludar_usuario(nombre_usuario)
print("")

 #3. Crear una función llamada informacion_personal(nombre, apellido,
 #edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 #[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
#dir los datos al usuario y llamar a esta función con los valores in
#gresados

def informacion_personal(nombre, apellido, edad, residencia):
   print(f"Soy {nombre} {apellido}, tengo {edad}, y vivo en {residencia}.")

nombre = input("Ingrese su nombre: ") 
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)
print("")
#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados

def calcular_area_circulo(radio):
   import math 
   return (math.pi)* radio **2 
   

def calcular_perimetro_circulo(radio):
   import math 
   return 2 * (math.pi) * radio

radio = int(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo (radio)
print(f"El area del circulo con un radio de {radio}, es {area} y el perimetro es {perimetro}.\n")


#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos
#trar el resultado usando esta función.

def segundos_a_horas(segundos):

   
    return (segundos //60) / 60
segundo= int(input("Ingrese una cantidad de ssegundoos para ser calculada en horas(Deben ser mas 3600s para llegar a una hora: "))

resultado = segundos_a_horas(segundo)
print(f"La cantidad de horas en {segundo} segundos es {resultado}\n")

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
#sultados de forma clara.
   
def operaciones_basicas(a, b):

   suma = a + b
   resta = a - b
   multiplicacion = a * b
   division = a / b

   if division != 0:
      division = a / b
   else:
      print("Nose puede dividir por 0.")

   return (suma, resta, multiplicacion, division)
   
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

resultados = operaciones_basicas(num1, num2)


print(f"Resultados de tus numeros {num1} y {num2}:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
#ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura): 
   imc = peso / (altura ** 2)
   return imc


peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

resultado_imc = calcular_imc(peso, altura)

print(f"Su IMC es: {resultado_imc:.2f}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función

def celsius_a_fahrenheit(celsius):
    """
    Convierte grados Celsius a grados Fahrenheit.
    Fórmula: F = (C * 9/5) + 32
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
resultado = celsius_a_fahrenheit(celsius)

print(f"{celsius:.2f}°C equivalen a {resultado:.2f}°F")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.
    
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

resultado = calcular_promedio(num1, num2, num3)

print(f"El promedio de los tres números es: {resultado:.2f}")
