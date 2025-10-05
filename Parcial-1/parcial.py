print ("Hola, este es el menu de opciones:")
print("1. Ingresar títulos.") 
print("2. Ingresar ejemplares. ")
print("3. Mostrar catálogo" )
print("4. Consultar disponibilidad.") 
print("5. Listar agotados") 
print("6. Agregar título")
print("7. Actualizar ejemplares (préstamo/devolución)")
print("8. Salir .")
titulos= []
ejemplares = []
opcion = ""

while opcion != "8":
    opcion = input("Ingrese el numero de la opcion que desea realizar. ")
    if opcion == "1":
        cantidad = int(input("Ingrese el numero de libros a ingresar: "))
        for titulo in range(cantidad):
            nombre_titulo= input("Ingrese el titulo del libro: ")
            titulos.append(nombre_titulo)
        print("Titulos cargados.")
    elif opcion == "2":
        if not titulos:
            print("Debe ingresar los titulos primero.")
        else:
             for i in range(len(titulos)):
                ejemplar = int(input(f"Ingrese la cantidad de ejemplares de {titulos[i]} "))
                ejemplares.append(ejemplar)
    elif opcion == "3":
        if not titulos or not ejemplares:
              print("Debe ingresar los titulos con sus ejempares primero.")
        else:
         for i in range(len(titulos)):
            print(f"Los libros y sus ejemplares son libro {i+1}:{titulos[i]} con {ejemplares[i]} ejemplares")
    elif opcion == "4":
        if not titulos:
              print("Debe ingresar los titulos primero.")
        else:
            titulo_especifico= input("Que titulo desea buscar? ").lower()
            titulo_encontrado= False
            for i in range(len(titulos)):
                if titulos[i] == titulo_especifico:
                    print(f"'{titulos[i]}' tiene {ejemplares[i]} ejemplares.")
                    titulo_encontrado = True
                    break
            if not titulo_encontrado:
                print("El titulo ingresado no se encuentra en el stock desponible")
    elif opcion == "5": 
        if 0 not in ejemplares:
            print("No hay ejemplares en 0")
        else:
            en_0 = []
            for i in range(len(ejemplares)):
                if ejemplares[i] == 0: 
                    en_0.append((titulos[i], ejemplares[i]))
            for titulo, i in en_0:
                print(f"{titulo} {i}")
    elif opcion == "6": 
        agrega = input("Agregar titulo: ")
        titulos.append(agrega)
        agrega_ej= int(input("Ingrese los ejemplares del libro añadido: "))
        ejemplares.append(agrega_ej)

    elif opcion == "7":
        if not titulos:
            print("No hay libros para actualizar. Ingrese un libro.")
        else:
            actualizacion = input("Que libro desea actualizar?: ")
            encontrado = False

        for i in range(len(titulos)):
            if titulos[i] == actualizacion:
                p_o_d = input("Ingrese 'prestamo' o 'devolucion' para realizar sobre el titulo: ").lower()
                
                if p_o_d == "prestamo":
                    if ejemplares[i] > 0:
                        ejemplares[i] -= 1
                        print(f"Se ha hecho un prestamo del libro: {titulos[i]}. Quedan {ejemplares[i]}.")
                    else:
                        print(f"No hay ejemplares disponibles de '{titulos[i]}'.")
                
                elif p_o_d == "devolucion":
                    ejemplares[i] += 1
                    print(f"Se ha hecho la devolucion del libro: {titulos[i]}. Ahora hay {ejemplares[i]}.")
                
                else:
                    print("Opcion no valida. Escriba 'prestamo' o 'devolucion'.")
                
                encontrado = True
                break  

        if not encontrado:
            print("El libro no se encuentra en el catalogo.")

print("Gracias!")