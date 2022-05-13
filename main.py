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

#Numero Elevado Al Cuadrado
print("Elevar Al Cuadrado")
numero1 = float(input("Digite El Numero A Elevar Al Cuadrado""\n"))
resultado = numero1 **2
print("La Elevacion Al Cuadrado es: " + str (resultado))

#Convertidor De Euros A Dolares
print("Convertidor De Euros A Dolares")
euros = float(input("Digite Sus Euros""\n"))
resultado = euros * 1.05
print("La Conversion De Euros A Dolares Es: " + str (resultado))

#Area Y Perimetro De Un Cuadrado
print("Area Y Perimetro De Un Cuadrado")
lado = float(input("Digite La Medida Del Lado Del Cuadrado""\n"))
area = lado **2
perimetro = 4 * lado
print("El perimetro es: " + str (perimetro))
print("El area es: " + str (area))

#Area Y Volumen De Un Cilindro
print("Area Y Volumen De Un Cilindro")
radio = int(input("Digite El Radio De Su Cilindro""\n"))
altura = int(input("Digite La Altura De Su Cilindro""\n"))
volumen = 3.14 * altura * radio **2
area = 2 * 3.14 * radio * radio + altura
print("El Volume Del cilindro es: " + str (volumen))
print("El area Del Cilindro es: " + str (area))

#Area Y Volumen De Un Circuferencia
print("Area Y Volumen De Un Cilindro")
radio = int(input("Digite El Radio De Su Cilindro""\n"))
altura = int(input("Digite La Altura De Su Cilindro""\n"))
longitud = 2 * 3.14 * radio **2
area = 3.14 * radio **2
print("El Volume Del cilindro es: " + str (longitud))
print("El area Del Cilindro es: " + str (area))


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

#Cual Es Mayor O Menor
print ("Digite Sus Dos Numeros Para Saber Cual Es Mayor O Menor")
numero1 = float(input("Digite Sus Numeros\n"))
print(str (numero1), ",")
numero2 = float(input(",\n"))
if (numero1<numero2): 
  print("El Numero " + str (numero1), "Es El Menor Que " + str (numero2) )
if (numero1>numero2): 
  print("El Numero " + str (numero1), "Es Mayor Que " + str (numero2) )

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

#A Y B Sumar Y Restar
print ("Digite Sus Dos Numeros")
numero1 = float(input("Digite Su Primer Numero\n"))
numero2 = float(input("Digite Su Segundo Numero\n"))
if (numero1<numero2): 
  print("El Numero " + str (numero2+numero1) )
if (numero1>numero2): 
  print("El Numero " + str (numero1-numero2) )

#El Cociente
print ("Digite Sus Dos Numeros")
dividiendo = float(input("Digite Su Dividiendo\n"))
divisor = float(input("Digite Su Divisor\n"))
if (divisor == 0):
  print("No Es Posible Dividir Por 0")
else:
  if ((dividiendo % divisor) == 0):
    print("El Cociente Es: " + str(dividiendo // divisor))

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