# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota mas alta y la mas baja.

notas = [7, 9, 4, 10, 6, 8, 5, 9, 3, 7]
print("Notas:", notas)

suma = 0
for nota in notas:
    suma = suma + nota

promedio = suma / len(notas)
print("Promedio:", promedio)

print("Nota mas alta:", max(notas))
print("Nota mas baja:", min(notas))

# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabeticamente. Investigue el uso del metodo sorted().
# • Preguntar al usuario que producto desea eliminar y actualizar la lista.

productos = []
for i in range(5):
    producto = input("Ingrese un producto: ")
    productos.append(producto)

print("Lista ordenada alfabeticamente:", sorted(productos))

eliminar = input("Que producto desea eliminar?: ")
if eliminar in productos:
    productos.remove(eliminar)
    print("Producto eliminado.")
else:
    print("El producto no esta en la lista.")

print("Lista actualizada:", productos)

numeros = []
for i in range(15):
    num = int(input("Ingrese un numero entero: "))
    numeros.append(num)

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Numeros ingresados:", numeros)
print("Pares:", pares)
print("Cantidad de pares:", len(pares))
print("Impares:", impares)
print("Cantidad de impares:", len(impares))

# 4) Dada una lista con valores repetidos
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

lista_con_repetidos = [4, 7, 2, 4, 9, 7, 1, 2, 8, 4]
lista_sin_repetidos = []

for valor in lista_con_repetidos:
    if valor not in lista_sin_repetidos:
        lista_sin_repetidos.append(valor)

print("Lista original:", lista_con_repetidos)
print("Lista sin repetidos:", lista_sin_repetidos)

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Alex", "Sofia", "Lautaro", "Daniel", "Carla", "Valentina", "Luna", "Cesar"]

print("Lista actual:", estudiantes)

opcion = input("Desea agregar o eliminar un estudiante? (escriba agregar o eliminar): ")

if opcion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print("Estudiante agregado.")
elif opcion == "eliminar":
    nombre = input("Ingrese el nombre del estudiante que desea eliminar: ")
    if nombre in estudiantes:
        estudiantes.remove(nombre)
        print("Estudiante eliminado.")
    else:
        print("Ese nombre no esta en la lista.")
else:
    print("Opcion no valida.")

print("Lista final:", estudiantes)

# 6) Dada una lista con 7 numeros, rotar todos los elementos una posicion hacia la derecha (el ultimo pasa a ser el primero).

numeros = [3, 7, 1, 9, 4, 6, 2]
print("Lista original:", numeros)

numeros = [numeros[-1]] + numeros[:-1]

print("Lista rotada:", numeros)

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas minimas y maximas de una semana.
# • Calcular el promedio de las minimas y el de las maximas.
# • Mostrar en que dia se registro la mayor amplitud termica.

# Formato: [ [min, max], [min, max], ... ] para 7 dias
temperaturas = [
    [12, 25],
    [10, 23],
    [14, 28],
    [9, 22],
    [11, 24],
    [13, 29],
    [8, 21]
]

suma_min = 0
suma_max = 0
mayor_amplitud = 0
dia_mayor_amplitud = 0

for i in range(7):
    t_min = temperaturas[i][0]
    t_max = temperaturas[i][1]
    suma_min += t_min
    suma_max += t_max
    amplitud = t_max - t_min
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1  

promedio_min = suma_min / 7
promedio_max = suma_max / 7

print("Promedio de minimas:", promedio_min)
print("Promedio de maximas:", promedio_max)
print("Dia con mayor amplitud termica:", dia_mayor_amplitud)

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
    [7, 8, 6],
    [5, 9, 7],
    [6, 6, 8],
    [9, 7, 7],
    [8, 6, 9]
]

print("Promedio por estudiante:")
for i in range(5):
    promedio = sum(notas[i]) / 3
    print("Estudiante", i + 1, ":", promedio)

print("Promedio por materia:")
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    promedio = suma / 5
    print("Materia", j + 1, ":", promedio)

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacias.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero despues de cada jugada.

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))

for turno in range(9):
    jugador = "X" if turno % 2 == 0 else "O"
    print("Turno del jugador", jugador)
    mostrar_tablero()
    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada. Turno perdido.")

    print()

mostrar_tablero()

# 10) Una tienda registra las ventas de 4 productos durante 7 dias, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el dia con mayores ventas totales.
# • Indicar cual fue el producto mas vendido en la semana.

ventas = [
    [10, 12, 11, 9, 14, 13, 15],   
    [8, 7, 9, 10, 11, 12, 13],    
    [5, 6, 7, 5, 6, 7, 8],         
    [15, 14, 13, 16, 12, 11, 10]   
]

print("Total por producto:")
totales_productos = []
for i in range(4):
    total = sum(ventas[i])
    totales_productos.append(total)
    print("Producto", i + 1, ":", total)


mayor_total = 0
dia_mayor = 0
for dia in range(7):
    total_dia = 0
    for prod in range(4):
        total_dia += ventas[prod][dia]
    if total_dia > mayor_total:
        mayor_total = total_dia
        dia_mayor = dia + 1  

print("Dia con mayores ventas:", dia_mayor)


mas_vendido = max(totales_productos)
indice = totales_productos.index(mas_vendido)
print("Producto mas vendido en la semana: Producto", indice + 1)
