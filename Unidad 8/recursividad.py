#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 

def factorial(num):
    if num == 0:
        return 1
    else: 
        return factorial(num-1)* num
    
numero = int(input("Ingrese un numero: "))
print(f"El factorial del numero ingresado es: {factorial(numero)}")

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1) + fibonacci(posicion-2)
posc = int(input("Ingrese un numero: ")) 
print(f"El numero de la serie de fibonacci de su numero es: {fibonacci(posc)}")
print("La serie de numeros hasta su numero es: ")
for i in range(0,posc+1):
    print(fibonacci(i))

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
#algoritmo general. 

def recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * recursiva(base, exponente -1)

base = int(input("Ingrese un numero base: "))
exponente = int(input("Ingrese un exponente: "))
print(f"La potencia de su numero es: {recursiva(base, exponente)}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto. 

def binario(num):
    if num == 0 or num == 1:
        return str(num)
    else: 
        return binario(num // 2) + str(num % 2)
numero = int(input("Ingrese un numero decimal: "))
print(f"Su numero en binario es: {binario(numero)}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es. 
#     Requisitos: 
#La solución debe ser recursiva. 
#No se debe usar [::-1] ni la función reversed(). 
def es_palindromo(palabra):
    if len(palabra) == 0  or len(palabra) == 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False 
    else:
        return es_palindromo(palabra[1:-1])
texto = input("Ingrese un texto sin espacios ni tildes: ").strip()
print (es_palindromo(texto))
