#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
#1450}
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}

precios_frutas['Naranja']= 1200
precios_frutas['Manzana']= 1500
precios_frutas['Pera']= 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800 

precios_frutas['Banana']= 1330
precios_frutas['Manzana']= 1700
precios_frutas['Melón']=2800

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

frutas = list(precios_frutas.keys())
print(frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe. 

#agenda = {}

#print("\n--Agenda telefonica--")

#for i in range(5):

 #   nombre = input("Ingrese un nombre: ")
 #   num = int(input("Ingrese el numero de telefono: "))
#    agenda[nombre] = num
#print("\nBuscar contacto en la agenda telefonica\n")

#contacto = input("Ingrese el nombre del contacto: ")
#if contacto in agenda:
 #   contacto_encontrado = agenda[contacto]
  #  print(f"Contacto:{contacto} numero:{contacto_encontrado}")
#else:
 #   print("El contacto no se encuentra en la lista.")

#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

frase_dividida= frase.split()

pablabras_unicas = set(frase_dividida)
print(f"Frase sin pablabras repetidas: {pablabras_unicas}")

conteo_palabras= {}
for palabra in frase_dividida:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1
    
for clave, valor in conteo_palabras.items():
    print(f"La cantidad de veces que aparece {clave} es {valor}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno.

#registro_alumnos = {}

#for i in range(3):
  #  print(f"\nAlumno n° {i + 1}")
    
   # nombre = input("Ingrese el nombre del alumno: ")
    
    #notas_lista = []
    
    #for i in range(3):
     #   while True:
      #      try:
       #         nota = float(input(f"  Ingrese la nota {i + 1}: "))
        #        if 0 <= nota <= 10:
         #           notas_lista.append(nota)
          #          break
           #     else:
           #         print("La nota debe estar entre 0 y 10.")
           # except ValueError:
            #    print("Entrada inválida. Por favor, ingrese un número.")

#notas_tupla = tuple(notas_lista)
    
 #   registro_alumnos[nombre] = notas_tupla

#for nombre, notas in registro_alumnos.items():
 #   suma_notas = sum(notas)
  #  promedio = suma_notas / i
    
   # print(f"El promedio de {nombre.capitalize()} es: {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial1 = {1,3, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2      # intersección
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2   # diferencia simétrica
print("Aprobaron solo uno:", solo_uno)

al_menos_uno = parcial1 | parcial2   # unión
print("Aprobaron al menos un parcial:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe.
stock = {
    "manzanas": 10,
    "naranjas": 8,
    "peras": 5
}

print("\nStock")
producto = input("Ingresá el nombre del producto: ").lower()

if producto in stock:
    print(f"El stock actual de {producto} es: {stock[producto]} unidades.")
    
    agregar = input("¿Querés agregar unidades? (si/no): ").lower()
    if agregar == "si":
        cantidad = int(input("¿Cuantas unidades queiere agregar?: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock[producto]}")
    else:
        print("No se realizaron cambios en el stock.")
else:
    print(f"El producto '{producto}' no existe en el inventario.")
    agregar_nuevo = input("¿Quiere agregarlo? (si/no): ").lower()
    if agregar_nuevo == "si":
        cantidad = int(input("Ingresa el stock inicial: "))
        stock[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")
    else:
        print("No se agrego el producto.")

print("\nInventario actualizado:")
for p, cant in stock.items():
    print(f"- {p}: {cant} unidades")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
#Permití consultar qué actividad hay en cierto día y hora. 
agenda = {
    ("lunes", "9:00"): "Reunión de equipo",
    ("martes", "14:00"): "Clase de inglés",
    ("miércoles", "18:30"): "Gimnasio",
    ("viernes", "20:00"): "Cena con amigos"
}

print("Consulta agenda")
dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (ej: 9:00, 14:00, etc.): ")

clave = (dia, hora)

if clave in agenda:
    print(f"A las {hora} del {dia} tienes: {agenda[clave]}")
else:
    print(f"No hay actividades registradas el {dia} a las {hora}.")

print("\nAgenda completa:")
for (d, h), evento in agenda.items():
    print(f"{d.capitalize()} a las {h}: {evento}")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

capitales = {capital: pais for pais, capital in paises.items()}

# Mostrar el resultado
print("Diccionario original (pais y capital):")
print(paises)

print("\nDiccionario invertido (capital y pais):")
print(capitales)
