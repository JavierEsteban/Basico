'''
Ejemplos básicos de tipos de datos...
'''

'''
Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
'''

valor = True
while(True):
    if (valor == True):
        nombre = input("ingrese su Nombre: ")
        print("Hola Mundo, Bienvenido {}".format(nombre))
    else:
        break
    valor = input("Deea continuar??...")



'''
Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y 
luego muestre por pantalla el contenido de la variable.
'''
Mensaje = "¡Hola Mundo!"
print(Mensaje)


'''
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y 
después de que el usuario lo introduzca muestre por pantalla la cadena
 ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
'''

nombre = str(input("Ingresar su Nombre: "))
print("Hola Mundo, {}".format(nombre))

'''
Ejercicio 4
Escribir un programa que pregunte el nombre del usuario en la consola 
y un número entero e imprima por pantalla en líneas distintas el nombre 
del usuario tantas veces como el número introducido.
'''

Nombre = str(input("Ingresar el Nombre: "))
Cantidad = int(input("Ingresar las cantidad de veces que se debe de repetir: "))

for i in range(Cantidad):
    print(Nombre)

'''
Ejercicio 5
Escribir un programa que pregunte el nombre del usuario en la consola y 
después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
'''
nombre = str(input("Ingresar el Nombre de la persona: "))
print("El Nombre es {} y la cantidad de digitos es {} .".format(nombre.upper(), nombre.__len__()))

'''
Ejercicio 6
Escribir un programa que realice la siguiente operación aritmética (3+22⋅5)2.
'''

ingrese= int(input("Ingrese un numero: "))
print( (ingrese + 22 + 5 ) * 2)

'''
Ejercicio 7
Escribir un programa que pregunte al usuario por el número de horas 
trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
'''

Horas = int(input("Ingrese el Número de Horas: "))
Costo = float(input("Ingrese el Costo por Horas: "))

print("La paga correspondiente: {}".format(Horas*Costo))

'''
Ejercicio 8
Escribir un programa que lea un entero positivo, 𝑛, 
introducido por el usuario y después muestre en pantalla la suma de todos 
los enteros desde 1 hasta 𝑛. La suma de los 𝑛 primeros enteros positivos puede 
ser calculada de la siguiente forma:

suma=𝑛(𝑛+1)2
'''


def sumatoria(numero):
    sumatotal = numero * (numero + 1) / 2
    return sumatotal


try:
    numero = int(input("Ingrese el número a realizar la operación: "))
    if (numero >= 0):
        suma = sumatoria(numero)
        print("La suma de los primeros 'n' numeros es : {}".format(suma))
    else:
        print("No ingresaron un número correcto..")
except:
    print("INgresar un nùmero")


'''
Ejercicio 9
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
es el índice de masa corporal calculado redondeado con dos decimales.
'''



try:

    peso = int(input("iNgrese su peso : "))
    altura = int(input(" INgrese su altura :"))
    if (peso < 0 or altura < 0):
        print("El peso o la altura debe de ser mayor q cero...")
    else:
        masa = peso / altura ** 2
        print("Tu índice de masa corporal es {} ".format(masa))
except:
    print("Ingrese correctamente el peso o la altura....")

'''
Ejercicio 10
Escribir un programa que pida al usuario dos números enteros y
 muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> 
 son los números introducidos por el usuario, y <c> y <r> son el cociente y 
 el resto de la división entera respectivamente.

'''

def calcula(n, m):
    try:
        respuestas = {}
        respuestas['divisionentera'] = n // m
        respuestas['divisionreal'] = n / m
        respuestas['residuo'] =n % m
    except:
        print("El segundo valor debe de ser mayor que cero....")
    return respuestas

try:
    n =float(input("Ingrese el primer Número "))
    m = float(input("Ingrese el segundo Número"))
    ver = str(input(""" Favor de colocar los que quieren calcular :
     residuo......................
     divisionentera .............
     divisionreal .............
    """))
    respuestasfinales = calcula(n, m)
    print("""El numero {} y el numero {}, 
           tienen la operacion de {} 
           es {}""".format(n, m, ver, respuestasfinales[ver]))
except:
    print("No ingresaron los valores correctos....")

'''
Ejercicio 11
Escribir un programa que pregunte al usuario una cantidad a invertir,
 el interés anual y el número de años, y 
 muestre por pantalla el capital obtenido en la inversión.

Formula de interes .. I = c * i * t
'''


def calculo_interes(c, t, i):
    if (c > 0 and i > 0 and t > 0):
        capital = c / (t * i)
    else:
        print("El valor debe de ser mayor que cero.....")
    return capital


cantidad = float(input("Ingrese el total ganado  ...... ... "))
tiempo = float(input("Ingrese el tiempo en años ......... "))
tasa = float(input("Ingrese la tasa de interes ............ "))
capital = calculo_interes(cantidad, tiempo, tasa)
print("El vaor del capital es {}".format(capital))

'''
Ejercicio 12
Una juguetería tiene mucho éxito en dos de sus productos: 
payasos y muñecas. Suele hacer venta por correo y 
la empresa de logística les cobra por peso de cada 
paquete así que deben calcular el peso de los 
payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos 
en el último pedido y calcule el peso total del paquete que será enviado.
'''


'''
Ejercicio 13
Imagina que acabas de abrir una nueva cuenta de 
ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero 
depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de 
ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
'''



'''
Ejercicio 14
Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de 
barras vendidas que no son del día. Después el programa 
debe mostrar el precio habitual de una barra de pan, 
el descuento que se le hace por no ser fresca y el coste final total.
'''
