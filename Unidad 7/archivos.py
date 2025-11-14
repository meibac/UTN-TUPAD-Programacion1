#1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
#productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad

lineas = [
    "Frutillas,500,5\n",
    "Durazno,300,4\n",
    "Pera,600,7\n"
    ]

with open("productos.txt","w") as archivo:
    archivo.writelines(lineas)

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
#formato:

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        datos = linea.split(",")
       
        producto = datos[0]
        precio = int(datos[1])
        cantidad = int(datos[2])
        
        print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}\n")

#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
#cantidad) y lo agregue al archivo sin borrar el contenido existente. 
# with open("productos.txt", "r") as archivo:
#     print("----Sus productos----")
#     for linea in archivo:
#         linea = linea.strip()
#         datos = linea.split(",")
        
#         producto = datos[0]
#         precio = int(datos[1])
#         cantidad = int(datos[2])

#         print(f"{producto} | Precio: ${precio} | Cantidad: {cantidad}")

#     print("\n--Ingrese un nuevo producto--")
#     nuevo_prod = input("Ingrese el nombre del producto: ")
#     nuevo_prec = input("Ingrese el precio del producto: ")
#     nuevo_cant = input("Ingrese la cantidad del producto: ")

# with open ("productos.txt", "a") as archivo:
#     archivo.write(f"{nuevo_prod},{nuevo_prec},{nuevo_cant}\n")
# print(f"Producto agregado con exito! Su producto: {nuevo_prod}, Precio: ${nuevo_prec}, Cantidad: {nuevo_cant}")
        
#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
#una lista llamada productos, donde cada elemento sea un diccionario con claves: 
#nombre, precio, cantidad. 

productos = []

with open ("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            'Producto:': nombre,
            'Precio: $': float(precio),
            'Cantidad':int(cantidad)
            })
print(productos)

#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
#no existe, mostrar un mensaje de error.

with open ('productos.txt', 'r') as archivo:
    producto = input("Ingrese el producto a buscar: ").lower()

    encontrado = False
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        
        if producto in nombre.lower():
            print(f"Su producto: {nombre}, precio: ${precio}, cantidad: {cantidad}\n")
            encontrado = True
            break
            
    else:
        print("No se encuentra el producto buscado.\n") 

#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
#productos actualizados desde la lista.

actualizados = []
with open('productos.txt', 'r') as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            actualizados.append({
            'nombre': nombre,
            'precio $': float(precio),
            'cantidad': int(cantidad)
            })

print("--OPCIONES A REALIZAR--")
print("1. Buscar producto")
print("2. Agregar producto")
print("3. Ver productos")
eleccion = input("Que desea hacer? ")

#buscar archivos.
if eleccion == "1":
    producto= input("Busque un producto: ").lower()
    encontrado = False
    for produc in actualizados:
        if producto in produc['nombre'].lower():
            print("Producto en la lista.")
            encontrado = True
            break
        
    else:
            print("Producto no encontrado")
elif eleccion == "2": #agregar productos 
        prod_nuevo = {}
        agregar_p= input("Ingrese un producto: ")
        agregar_prec = input("Precio: ")    
        agregar_c = input("Cantidad: ")
        
        prod_nuevo = {
             'nombre': agregar_p,
             'precio $': float(agregar_prec),
             'cantidad': int(agregar_c)
        }
        actualizados.append(prod_nuevo)
elif eleccion == "3":
     print("LISTA DE PRODUCTOS: ", actualizados)

with open ('productos.txt', 'w') as archivo:
    for producto in actualizados: 
        nombre = producto['nombre'] 
        precio = producto['precio $']
        cantidad = producto['cantidad']
        cadena = str(f"{nombre},{precio},{cantidad}\n")
        
        archivo.write(cadena)