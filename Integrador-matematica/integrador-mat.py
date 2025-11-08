#Tema: Conversor de numeros decimales a binarios y de binarios a decimales.   

#Pedimos al un numero al usuario para convertir de decimal a binario.

num= int(input("Ingrese un numero para ver su conversion a binario: "))
if num < 0:
    print("Por favor ingrese un numero entero positivo.")
else:
    binario= ""
    if num == 0:
        binario = "0"
    else:
        while num > 0 :
            resto = num % 2
            binario = str(resto) + binario 
            num =  num // 2


print("el numero binario es:", binario)

#Convertir de binario a decimal.

num= (input("Ingrese un numero binario para ver su conversion a decimal: "))

es_binario = True
for i in num: 
    if i != "0" and i != "1":
        es_binario = False
        break
if es_binario: 
    resultado = 0   
    longitud = len(num)
    
    for i in range(longitud):  
        poten = longitud - i - 1
        digito = int(num[i])
        resultado = resultado + digito *(2**poten)
    print(f"El numero binario {num} en decimal es: {resultado}")
else:
    print("Debe ingresar un numero binario valido.")