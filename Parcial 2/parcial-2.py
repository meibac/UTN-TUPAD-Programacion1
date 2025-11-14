import csv
import os

def cargar_catalogo(nombre_archivo):#cargamos el archivo.
    catalogo = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                titulo = fila['TITULO'].strip()
                cantidad = int(fila['CANTIDAD'])
                catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    else:
        catalogo = []
    return catalogo
def guardar_catalogo(nombre_archivo, catalogo): #guardamos catalogo de libros
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
        campos = ['TITULO', 'CANTIDAD']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for libro in catalogo:
            escritor.writerow(libro)


def normalizar_titulo(titulo):
    return " ".join(titulo.strip().lower().split())

def buscar_libro(catalogo, titulo): #buscamos el libro
    t = normalizar_titulo(titulo)
    for i in range(len(catalogo)):
        if normalizar_titulo(catalogo[i]['TITULO']) == t:
            return i
    return -1



def ingresar_titulos(catalogo, archivo): #para cantdad de libros
    n = input("Cuantos libros desea ingresar? ")
    if not n.isdigit() or int(n) <= 0:
        print("Cantidad invalida.")
        return
    n = int(n)

    for _ in range(n): #verificacon de titulo
        titulo = input("Titulo del libro: ").strip()
        while titulo == "" or buscar_libro(catalogo, titulo) != -1:
            if titulo == "":
                print("El titulo no puede estar vacio.")
            else:
                print("Ese titulo ya existe.")
            titulo = input("Ingrese otro titulo: ").strip()

        cantidad = input("Cantidad de ejemplares: ")
        while not cantidad.isdigit() or int(cantidad) < 0:
            cantidad = input("Cantidad invalida. Intente nuevamente: ")
        cantidad = int(cantidad)

        catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})

    guardar_catalogo(archivo, catalogo)
    print("Libros cargados correctamente.\n")


def ingresar_ejemplares(catalogo, archivo): # se ingresan los ejemplares 
    titulo = input("Titulo del libro: ").strip()
    i = buscar_libro(catalogo, titulo)
    if i == -1:
        print("Libro no encontrado.")
        return
    cant = input("Cantidad a agregar: ")
    while not cant.isdigit() or int(cant) <= 0:
        cant = input("Ingrese una cantidad valida: ")
    catalogo[i]['CANTIDAD'] += int(cant)
    guardar_catalogo(archivo, catalogo)
    print("Ejemplares actualizados.\n")


def mostrar_catalogo(catalogo): #muestra el catalogo
    if len(catalogo) == 0:
        print("Catalogo vacio.\n")
        return
    print("\n--- CATALOGO ---")
    for libro in catalogo:
        print(f"{libro['TITULO']} -> {libro['CANTIDAD']} ejemplares")
    print()


def consultar_disponibilidad(catalogo): #disponibilidad
    titulo = input("Titulo a consultar: ").strip()
    i = buscar_libro(catalogo, titulo)
    if i == -1:
        print("Libro no encontrado.\n")
    else:
        print(f"Disponibles: {catalogo[i]['CANTIDAD']}\n")


def listar_agotados(catalogo):
    agotados = [l for l in catalogo if l['CANTIDAD'] == 0]
    if not agotados:
        print("No hay libros agotados.\n")
    else:
        print("\n--- LIBROS AGOTADOS ---")
        for l in agotados:
            print(l['TITULO'])
        print()


def agregar_titulo(catalogo, archivo): # agrega titulo y verifica
    titulo = input("Titulo: ").strip()
    if titulo == "" or buscar_libro(catalogo, titulo) != -1:
        print("Titulo invalido o duplicado.")
        return
    cant = input("Cantidad inicial: ")
    while not cant.isdigit() or int(cant) < 0:
        cant = input("Cantidad invalida: ")
    catalogo.append({"TITULO": titulo, "CANTIDAD": int(cant)})
    guardar_catalogo(archivo, catalogo)
    print("Libro agregado.\n")


def actualizar_ejemplares(catalogo, archivo): #para actualizar 
    titulo = input("Titulo: ").strip()
    i = buscar_libro(catalogo, titulo)
    if i == -1:
        print("Libro no encontrado.")
        return

    print("1. Prestamo (restar 1)\n2. Devolucion (sumar 1)")
    op = input("Opcion: ")

    if op == "1":
        if catalogo[i]['CANTIDAD'] > 0:
            catalogo[i]['CANTIDAD'] -= 1
            print("Prestamo registrado.")
        else:
            print("No hay ejemplares disponibles.")
    elif op == "2":
        catalogo[i]['CANTIDAD'] += 1
        print("Devolucion registrada.")
    else:
        print("Opcion invalida.")
        return

    guardar_catalogo(archivo, catalogo)
    print()


# ---------- MENU PRINCIPAL ----------

def menu():
    ARCHIVO = "catalogo.csv"
    catalogo = cargar_catalogo(ARCHIVO)

    while True:
        print("=== MENU BIBLIOTECA ===")
        print("1. Ingresar titulos (multiples)")
        print("2. Ingresar ejemplares")
        print("3. Mostrar catalogo")
        print("4. Consultar disponibilidad")
        print("5. Listar agotados")
        print("6. Agregar titulo individual")
        print("7. Actualizar ejemplares (prestamo/devolucion)")
        print("8. Salir")

        op = input("Seleccione una opcion: ")
        print()

        if op == "1":
            ingresar_titulos(catalogo, ARCHIVO)
        elif op == "2":
            ingresar_ejemplares(catalogo, ARCHIVO)
        elif op == "3":
            mostrar_catalogo(catalogo)
        elif op == "4":
            consultar_disponibilidad(catalogo)
        elif op == "5":
            listar_agotados(catalogo)
        elif op == "6":
            agregar_titulo(catalogo, ARCHIVO)
        elif op == "7":
            actualizar_ejemplares(catalogo, ARCHIVO)
        elif op == "8":
            print("Fin del programa.")
            break
        else:
            print("Opcion invalida.\n")


# ---------- INICIO DEL PROGRAMA ----------

menu()