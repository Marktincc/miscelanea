
#Area De Un Trinagulo
print("Digite Sus Datos Para Calcular La Base De Un Triangulo.")
base = float(input("Base?\n"))
altura = float(input("Altura?\n"))
resultado = base * altura / 2
print("La Area De Su Triangulo Es: " + str (resultado))

#Suma De Dos Numeros Por Teclado
print("Digite sus numeros para realizar la suma?")
suma1 = int(input("\n"))
print( str (suma1),  "+")
suma2 = int(input())
resultado = suma1 + suma2
print( str (suma1),  "+", str (suma2), "=", str(resultado) )
print("La suma es: " + str (resultado))
  #Optimizado Codigo
def total (valor1, valor2):
  resultado = valor1 + valor2
  print(f"El Resultado De La Suma Es: {resultado}")
total(int(input("Digite El Primer Valor: ")), int(input("Digite El Segundo Valor: ")))

#Numero Elevado Al Cuadrado
print("Elevar Al Cuadrado")
numero1 = float(input("Digite El Numero A Elevar Al Cuadrado""\n"))
resultado = numero1 **2
print("La Elevacion Al Cuadrado es: " + str (resultado))
  #Optimizado Codigo
def cuadrado (numero1):
    resultado = numero1 ** 2
    print(f"El Numero Al Cuadrado Es: {resultado}")
cuadrado(float(input("Digite El Numero A Elevar Al Cuadrado: ")))

#Convertidor De Euros A Dolares
print("Convertidor De Euros A Dolares")
euros = float(input("Digite Sus Euros""\n"))
resultado = euros * 1.05
print("La Conversion De Euros A Dolares Es: " + str (resultado))
  #Optimizado Codigo
def euros (valor1):
    convertidor = valor1 * 1.05
    print(f"La Conversion De Euros A Dolares Es: {convertidor}")
euros(float(input("Digite La Cantindad De Euros Que Decea Convertir: ")))

#Area Y Perimetro De Un Cuadrado
print("Area Y Perimetro De Un Cuadrado")
lado = float(input("Digite La Medida Del Lado Del Cuadrado""\n"))
area = lado **2
perimetro = 4 * lado
print("El perimetro es: " + str (perimetro))
print("El area es: " + str (area))
  #Optimizado Codigo
def area_perimetro (lado):
    area = lado ** 2
    perimetro = 4 * lado
    print(f"El Area Del Cuadrado Es: {area}\n"f"El Perimetro Del Cuadrado Es: {perimetro}")
area_perimetro(int(input("El Tamaño Del Cuadrado: ")))
#Area Y Volumen De Un Cilindro
print("Area Y Volumen De Un Cilindro")
radio = int(input("Digite El Radio De Su Cilindro""\n"))
altura = int(input("Digite La Altura De Su Cilindro""\n"))
volumen = 3.14 * radio ** 2 * altura
area = ((2 * 3.14 * radio * altura) + (3.14 * radio ** 2 * altura))
print("El Volume Del cilindro es: " + str (volumen))
print("El area Del Cilindro es: " + str (area))
  #Optimizado Codigo
def area_volumen (radio, altura):
    volumen = 3.14 * radio ** 2 * altura
    area = ((2 * 3.14 * radio * altura) + (3.14 * radio ** 2 * altura))
    print(f"El Area Del Cilindro Es: {area}\n"f"El Volumen Del Cilindro Es: {volumen}")
area_volumen(float(input("Digite El Radio Del Cilindro: ")),float(input("Digite La Altura Del Cilindro: ")))

#Area Y Volumen De Un Circuferencia
print("Area Y Perimetro De Un Circuferencia")
radio = int(input("Digite El Radio De Su Circunferencia""\n"))
area = 3.14 * radio **2
perimetro = 2 * 3.14 * radio
print("El Area De La Circunferencia es: " + str (area))
print("La Longitud De la Circunferencia es: " + str (perimetro))
  #Codigo Optimizado
def area_perimetro (radio):
    area = 3.14 * radio ** 2
    perimetro = 2 * 3.14 * radio
    print(f"El Area De Su Circunferencia: {area}\n"f"El Perimetro De Su Circunferencia Es: {perimetro}")
area_perimetro(float(input("Digite El Radio De Su Circuferencia: ")))

#Calcular Promedio De Tres Numeros
print("Promedio de tres numeros")
valor1 = int(input("Digite Sus Tres Numeros""\n"))
print( str (valor1),",")
valor2 = int(input())
print( str (valor1),",",str (valor2),"y")
valor3 = int(input())
print( str (valor1),",",str (valor2),"y", str (valor3))
promedio = valor1 + valor2 + valor3 / 3
print("El Promedio De Sus Tres Numeros Es: " + str (promedio))
  #Codigo Optimizado
total = 0
for i in range(3):
    valor = int(input(f"Digite Su Valor {i + 1} : "))
    total += valor
    resultado = total / 3
print (f"El Promedio De Los Tres Números Es: {resultado}")


#Condiconales




#Positivo O Negativo
print ("Saber Si Su Numero Es Negativo O Positivo")
numero1 = float(input("Digite Su Digito?\n"))
if (numero1 > 0):
    print("El Numero " + str (numero1), "Es Positivo" )
if (numero1 < 0):
    print("El Numero " + str (numero1), "Es Negativo" )
if (numero1 == 0):
    print("El Numero " + str (numero1), "Es Neutro" )
  #Codigo Optimizado
def negativo_o_positivo (valor1):
    if valor1 < 0:
        print(f"El Numero {valor1} Es Negativo")
    else:
        print(f"El Numero {valor1} Es Positivo")

negativo_o_positivo(int(input("Digite Su Numero: ")))


#Cual Es Mayor O Menor
print ("Digite Sus Dos Numeros Para Saber Cual Es Mayor O Menor")
numero1 = float(input("Digite Sus Numeros\n"))
print(str (numero1), ",")
numero2 = float(input(",\n"))
if (numero1<numero2): 
  print("El Numero " + str (numero1), "Es El Menor Que " + str (numero2) )
if (numero1>numero2): 
  print("El Numero " + str (numero1), "Es Mayor Que " + str (numero2) )
  #Codigo Optimizado
def mayor_menor (valor1, valor2):
    if valor1 < valor2 :
        print(f"El Numero Mayor Es {valor2} El Menor Es {valor1}")
    else:
        print(f"El Numero Mayor Es {valor1} El Menor Es {valor2}")
mayor_menor(int(input("Digite Su Numero: ")),(int(input("Digite Su Segundo Numero: "))))

#Tres Numeros Menor Y Mayor
print ("Digite Sus Tres Numeros")
numero1 = float(input("Digite Su Primer Numero\n"))
numero2 = float(input("Digite Su Segundo Numero\n"))
numero3 = float(input("Digite Su Tercer Numero\n"))
list = [numero1, numero2, numero3]
list.sort()
menor = (list[0])
mayor = (list[2])
print ("El Numero Menor Es" ,str(menor), "El Numero Mayor Es" , str(mayor))
  #Codigo Opitimizado
def mayor_menor (valor1, valor2, valor3):
    list = [valor1,valor2,valor3]
    list.sort()
    numero_menor, numero_mayor = (list[0]),(list[2])
    print(f"El Numero Menor Es {numero_menor} Y El Numero Mayor Es {numero_mayor}")
mayor_menor((int(input("Digite Su Primer Numero: "))),(int(input("Digite Su Segundo Numero: "))),(int(input("Digite Su Tercer Numero: "))))
#A Y B Sumar Y Restar
print ("Digite Sus Dos Numeros")
numero1 = float(input("Digite Su Primer Numero\n"))
numero2 = float(input("Digite Su Segundo Numero\n"))
if (numero1<numero2): 
  print("El Numero " + str (numero2+numero1) )
if (numero1>numero2): 
  print("El Numero " + str (numero1-numero2) )
  #Codigo Optimizado
def sumar_restar (valor1,valor2):
    if valor1 < valor2:
        print(f"La Suma Es {valor2+valor1}")
    else:
        print(f"La Resta Es {valor1-valor2}")
sumar_restar((int(input("Digite Su Primer Numero: "))),(int(input("Digite Su Segundo Numero: "))))

#El Cociente
print ("Digite Sus Dos Numeros")
dividiendo = float(input("Digite Su Dividiendo\n"))
divisor = float(input("Digite Su Divisor\n"))
if (divisor == 0):
  print("No Es Posible Dividir Por 0")
else:
  if ((dividiendo % divisor) == 0):
    print("El Cociente Es: " + str(dividiendo // divisor))
 #Codigo Optimizado
def division (dividiendo, divisor):
    if divisor == 0:
        print("No Es Posible Dividir Por 0")
    else:
        print(f"El Conciente Es: {dividiendo/divisor}")
division((int(input("Digite Su Dividiendo: "))),(int(input("Digite Su Divisor: "))))

#Sumarlos Si Uno Es Negativo Multiplicarlos Si Los Dos Son Positivos
print("Sumar Si Uno De Numeros Sus Numeros Es Negativo O Multiplicarlos Si Los Dos Son Positivos")
valor1= int(input("Digite Su Numero\n"))
print((valor1), "y ")
valor2= int(input(""))
if ((valor1<0) or (valor2<0)):
      print (valor1+valor2)
else:
  if ((valor1 or valor2 ) > 0):
    print(valor1*valor2)

#Si Un Año No Es Biciesto o Si Es Bisiesto
año = int(input("Digite Su Año \n"))
if (año % 4 == 0 and (año % 100 != 0)) or (año % 400 == 0):
  print("El Año", str(año),"Es Bisiesto")
else:
  print("El Año", str(año),"No Es Bisiesto")
 #Codigo Optimizado
def biciesto (año):
    if (año % 4 == 0 and (año % 100 != 0)) or (año % 400 == 0):
        print(f"El Año {año} Es Bisiesto")
    else:
        print(f"El Año {año} No Es Bisiesto")
biciesto((int(input("Digite El Año: "))))
#Ciclos

#Imprimir Los Multiplos De # Que Hay Del 1 Al 100
multiplos = 3
while multiplos < 100:
  print(multiplos)
  multiplos += 3

#Imprimir Todos Los Numeros Impares Del 0 al 100
multiplos = 1
while multiplos < 100:
  print(multiplos)
  multiplos += 2
  
#Imprimir Todos Los Numeros Pares Del 1 al 100
multiplos = 2
while multiplos < 100:
  print(multiplos)
  multiplos += 2

#Cuadrados Del 1 Al 30
for x in range (1,31,1):
  x = x ** 2
  print (x)

#Cuadraddo De Los 100 Primero Numeros Y EL Total
total = 0
for x in range (1,101,1):
  x = x**2
  total = total + x
  print(total)

#Dar Dos Numeros El Primero Menor Que El Segundo
valor1 = int(input("Digite Un Numero\n"))
valor2 =  int(input("Digite Un Numero Mayor Que El Anterior\n"))
print ("Los Numeros Que Se En Cuentran En Entre Estos Valores Son:")
for x in range (valor1,valor2):
  x = x
  print (x)

#Sumar Todos Los Numeros Que Se Digan Por Teclado
valor = 1
total = 0
while valor != 0 :
  valor1 = int(input("Digite Los Numeros Que Desea Sumar\n"))
  if valor1 == 0 :
    valor = 0
  else :
    total = total + valor1
  print (total)


#1.1
valor = 1
total = 0
while valor != 0 :
  valor1 = int(input("Digite El Numeros Que Desea Sumar\n"))
  if valor1 == 0 :
    valor = 0
  else :
    total = total + valor1
    print ("La Suma Que Llevas Es: ",(total))
print("El Resultado De La Suma Es: ", (total))
#Arreglos

#1

import random
lista = []
numeros = (int(input("Digite El Rango: \n")))
for i in range(numeros):
    enteros = int(random.randint(-100, 100))
    lista.append(enteros)
def bubbleSort(lista):
    enteroslist = len(lista)
    for i in range(enteroslist - 1):
        for n in range(0, enteroslist - i - 1):
            if lista[n] > lista[n + 1]:
                lista[n], lista[n + 1] = lista[n + 1], lista[n]
    return lista
print(bubbleSort(lista))
print ()

#Elabore una aplicacion que permita introducir 20 elementos de mayor a menor

lista = []
print("Digite Sus 20 Numeros")
valores = 20
valor1 = 0
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Elemento")
    enteros = int(input())
    lista.append(enteros)
    valor1 += 1
lista.sort(reverse=True)
print(("El Orden De Sus Elementos Esta De Mayor A Menor\n"), (lista))


#3

lista = []
lista1 = []
lista3 = []
print("Digite Sus 10 Numeros")
valores = 10
valor1 = 0
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Numeros")
    enteros = int(input())
    lista.append(enteros)
    lista1.append(enteros)
    lista3.append(enteros)
    valor1 += 1
lista.sort(reverse=True)
lista1.sort()
print("Los Numeros Que Digito Son\n", str(lista3))
print(("El Orden De Sus Digitos Esta De Menor A Mayor\n"), str (lista1))
print(("El Orden De Sus Digitos Esta De Mayor A Menor\n"), str (lista))

#4

arreglo = [75, 3, 1, 54, 654, 87, 213, 0],
for posicion in arreglo:
    maximo = max(posicion)
    posicionmax = posicion.index(maximo)
    menor = min(posicion)
    posicionmin = posicion.index(menor)
print("El Arreglo Es: \n",str (arreglo))
print("El Valor Maximo Del Arreglo Es: ", str (maximo), "Y La Ubicacion Dentro Del Arreglo Es: ", str (posicionmax))
print("El Valor Minimo Del Arreglo Es: ", str (menor), "Y La Ubicacion Dentro Del Arreglo Es: ", str (posicionmin))

#5

lista = []
print("Digite Sus 10 Numeros")
valores = 10
valor1 = 0
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Numeros")
    enteros = int(input())
    lista.append(enteros)
    valor1 += 1
caracter1 = []
for i in lista:
    caracter = "*"
    a = (caracter * i)
    caracter1.append(a)
for n,c in zip(lista, caracter1):
    print (str(n)+ ":"+(c))

#6

lista = []
print("Digite Sus 25 Numeros")
valores = 25
valor1 = 0
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Numeros")
    enteros = int(input())
    lista.append(enteros)
    valor1 += 1
print("El Arreglo Que Digitaste Fue :\n", (lista))
repetido=int(input("Digite El Numero Para Saber Cuantas Veces Se Encuentra En El Arreglo\n"))
cantidad = lista.count(repetido)
print("Las Veces Que Este Numero Esta Repetido En El Arreglo Es: ", (cantidad))

#7


print("Digite Sus 8 Numeros")
valores = 8
valor1 = 0
impar = []
par = []
lista = []
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Numeros")
    enteros = int(input())
    lista.append(enteros)
    valor1 += 1
for i in range(valores):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
      impar.append(lista[i])
impar.sort()
par.sort()
print("El Arreglo Que Diste Fue: \n"+ str(lista),"\n""Los Numeros Impares Del Arreglo Son: \n"+ str(impar),"\n""Los Numeros Pares Del Arreglo Son: \n"+ str(par))



