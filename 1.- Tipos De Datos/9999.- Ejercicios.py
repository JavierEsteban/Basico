
'''
Ejercicios para estructura if
Ejercicio 1
Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.


Numero1 = int(input("Ingrese el Primer Número : "))
Numero2 = int(input("Ingrese el Primer Número : "))


if Numero1 > Numero2 :
    print("El Número {}, es mayor que {}".format(Numero1,Numero2))
else :
    print("El Número {}, es Menor que {}".format(Numero1,Numero2))



Ejercicio 2
Algoritmo que pida un número y diga si es positivo, negativo o 0.


Numero = int(input("Ingrese un Número a Analizar : "))

if Numero < 0:
    print("El número es Negativo")
elif Numero > 0:
    print("El número es Positivo")
elif Numero == 0:
    print("El número es Neutro")



Ejercicio 3
Escribe un programa que lea un número e indique si es par o impar.


Listado = list()
ListadoAnalizado = list()
Pregunta = 'S'

while (Pregunta == 'S'):
    Listado.append(int(input("Favor de Ingresar el Número a Analizar :")))
    Pregunta = input("Favor de Indicar si desea continuar (S o N) : ")


for i in range (0,len(Listado)):
    if Listado[i] % 2 == 0:
        ListadoAnalizado.append('Par')
        print("El número analizado {} es par.".format(Listado[i]))
    else:
        ListadoAnalizado.append('Impar')
        print("El número analizado {} es impar.".format(Listado[i]))

print(Listado)
print(ListadoAnalizado)

Ejercicio 4
Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero,
o un mensaje de aviso en caso contrario.

ListadoNumero = list()
contador = 0
while contador <= 1 :
    ListadoNumero.append(int(input("Ingrese el Valor a Analizar : ")))
    contador = contador + 1

if ListadoNumero[1] == 0 :
    print("El Número del divisor es cero, no se puede dividir .")
else :
    Division = ListadoNumero[0] / ListadoNumero [1]
    print("La division es : " + str(Division))

Ejercicio 5
Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe”
    y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

Conteo = 0

while (True):
    Nombre = str(input("Usuario : "))
    Pass = str(input("Pass : "))
    if Nombre == "pepe" and Pass == "asdasd" :
        print("Usuario y Nombre Correcto, Puede acceder al Sistema : Bienvenido {} . ".format(Nombre))
        break
    elif Conteo == 2 :
        print("El número de intentos superó los máximos permitidos : ")
        break
    print("Usuario {} o Clave {} , Incorrecta favor de volver a validar : ".format(Nombre, Pass))
    Conteo = Conteo + 1



Ejercicio 6
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.


BaseDatos = ['A','B','C']
CadenaAnalizada = str ( input("Favor de ingresar una cadena de Texto : "))

print(len(CadenaAnalizada))

for i  in range (0, len(CadenaAnalizada)) :
    if CadenaAnalizada[i] in BaseDatos :
       print("Se encontro el Primero {} valor en Mayusculas . ".format(CadenaAnalizada[i]))



Ejercicio 7
Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
El exponente sea positivo, sólo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.


def ExpPositivo(Numero, Exponente) :
        return "ExpPositivo"
                #pow(Numero, Exponente)

def ExpCero(Numero, Exponente) :
        return "ExpCero"
                #1

def ExpNegativo (Numero, Exponente) :
        return "ExpNegativo"
                #pow(Numero, 1/ Exponente )



Numero = int(input("Ingrese el Valor de la Base : "))
Exponente = int(input("Ingrese el Valor del Exponente : "))

print("Operaciones Posibles : \n1.- Exponente Positivo \n2.- Exponente Negativo \n3.- ExponenteNeutro")
Switch = { 1  : "ExpPositivo",  2  : "ExpNegativo",  3  : "ExpCero"}

Seleccion = int(input("Favor de elegir una opcion en números : "))

print(Numero, Exponente, Seleccion)
print( Switch[Seleccion](Numero,Exponente ) )
#Resultado = Switch(Seleccion,(2,3))
#Resultado = Switch[Seleccion](int(Numero), int(Exponente))
#print(Resultado)


Ejercicio 8
Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el
mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a
dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe
imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.




nota = int(input("Insertar la Nota : "))
edad = int(input("Insertar la Edad : "))
sexo = str(input("Insertar la Sexo : "))

#edad >= 5  o edad >= 18 y sexo femenino -> aceptada
#edad >= 18 y sexo m -> Posible
#en caso contrario no aceptada

if nota >= 5:
        if edad >= 18 and sexo == 'F':
                print("Aceptada :) ")
elif nota >= 5:
        if edad >= 18 and sexo == 'M' :
                print("Posible")
else :
        print("No Aceptada :(")

Ejercicio 9
Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);


numero1 = int(input("Ingrese el Primer Número : "))
numero2 = int(input("Ingrese el Segundo Número : "))
numero3 = int(input("Ingrese el Tercer Número : "))

if numero1 >= numero2:
        if numero2 >= numero3:
                print("Los números se ordenan de la siguiente Forma : {}, {}, {}".format(numero1, numero2, numero3))
        elif numero2 < numero3:
                print("Los números se ordenan de la siguiente Forma : {}, {}, {}".format(numero1, numero3, numero2))
elif numero1 >= numero3:
        if numero2 >= numero3:
                print("Los números se ordenan de la siguiente Forma : {}, {}, {}".format(numero1, numero2, numero3))
        elif numero2 < numero3:
                print("Los números se ordenan de la siguiente Forma : {}, {}, {}".format(numero1, numero3, numero2))
else:
        if numero2 >= numero3:
                print("Los números se ordenan de la siguiente Forma : {}, {}, {}".format(numero2, numero3, numero1))
        elif numero2 < numero3:
                print("Los números se ordenan de la siguiente Forma : {}, {}, {}".format(numero3, numero2, numero1))

Ejercicio 10
Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
circunferencias y las clasifique en uno de estos estados:

exteriores

tangentes exteriores

secantes

tangentes interiores

interiores

concéntricas



Ejercicio 11
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

Si se cumple Pitágoras entonces es triángulo rectángulo

Si sólo dos lados del triángulo son iguales entonces es isósceles.

Si los 3 lados son iguales entonces es equilátero.

Si no se cumple ninguna de las condiciones anteriores, es escaleno.

def descubretriangulo(lado1, lado2, lado3):

        if (lado1 == lado2) or (lado2 == lado3):
                if (lado2 == lado3):
                        print("Es un Triangulo Equilatero.")
                elif (lado2 != lado3):
                        print("Es un Triangulo Isosceles.")
        elif (lado1 != lado2) or (lado2 != lado3):
                if ( pow(lado1 , 2) + pow(lado2, 2) ) == pow(lado3, 2):
                        print("Es un Triangulo Rectangulo.")
                else:
                        print("Es un Triangulo Escaleno.")


n1 = int(input("Ingresar el primer lado: "))
n2 = int(input("Ingresar el primer lado: "))
n3 = int(input("Ingresar el primer lado: "))

descubretriangulo(n1, n2, n3)


Ejercicio 12
Escribir un programa que lea un año indicar si es bisiesto.
Nota: un año es bisiesto si es un número divisible por 4,
pero no si es divisible por 100, excepto que también sea divisible por 400.



#Definicion de función de anios Bisiestos.
def Bisiesto(anio):
       if (anio % 4 == 0) and (anio % 100 == 0):

               if(anio % 400 == 0):
                       return 'SI'
               elif(anio % 400 != 0):
                       return 'NO'

anio = int(input("Ingrese año a realizar el analisis :"))
print(Bisiesto(anio))


Ejercicio 13
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

#Declaracion  de Diccionarios de meses
meses = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
}

#Definicion de función de anios Bisiestos.
def Bisiesto(anio):
       if (anio % 4 == 0) and (anio % 100 == 0):

               if(anio % 400 == 0):
                       return 'SI'
               elif(anio % 400 != 0):
                       return 'NO'

anio = int(input("Ingrese año a realizar el analisis :"))
mes = int(input("Ingrese el mes a realizar el analisis : "))
dia = int(input("Ingrese el día a realizar el analisis : "))


revisaranio = Bisiesto(anio)


if (mes > 0) and (mes <= 12):
        if (dia >0) and (dia <= 31):
                if(revisaranio == 'SI'):
                        if (mes == 2):
                                if (meses.get(mes) + 1 < dia):
                                        print("Fecha Incorrecta")
                else:
                        print("Fecha Correcta")
        else:
                print("Fecha Incorrecta")

else:
        print("Fecha Incorrecta")


Ejercicio 14
La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva,
la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto,
ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque,
considerando lo siguiente:

si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2.

Si es de tipo B,
se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2.

Realice un algoritmo para determinar la ganancia obtenida.


# Tipos de Uva : A , B
# Tamaño de Uva : 1, 2

Pinicial = 10
tipo = str(input("Ingresar Tipo de Uva : "))
Tamanio = int(input("Ingresar Tamaño de Uva : "))
Cantidad = int(input("Ingrese la Cantidad de Uva para el embarque : "))

if(tipo in ('A' ,'B')):
        if (Tamanio in (1, 2)):
                if (tipo == 'A'):
                        if (Tamanio == 1):
                                Total = (Pinicial + 0.2) * Cantidad
                                Ganancia = 0.2*Cantidad
                                print("El total es {}, La ganancia obtenida es {} .".format(Total, Ganancia))
                        elif (Tamanio == 2):
                                Total = (Pinicial + 0.3) * Cantidad
                                Ganancia = 0.3*Cantidad
                                print("El total es {}, La ganancia obtenida es {} .".format(Total, Ganancia))
                else:
                        if (Tamanio == 1):
                                Total = (Pinicial + 0.3) * Cantidad
                                Ganancia = 0.3*Cantidad
                                print("El total es {}, La ganancia obtenida es {} .".format(Total, Ganancia))
                        elif (Tamanio == 2):
                                Total = (Pinicial + 0.5) * Cantidad
                                Ganancia = 0.5*Cantidad
                                print("El total es {}, La ganancia obtenida es {} .".format(Total, Ganancia))
        else:
                print("Tamaño de Uva Incorrecta....")
else:
        print("Tipo de Uva Erronea Vuelvelo a Intentar.....")

Ejercicio 15
El director de una escuela está organizando un viaje de estudios,
y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio.
La forma de cobrar es la siguiente:
si son 100 alumnos o más, el costo por cada alumno es de 65 euros;
de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros,
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.

Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.
'''



'''
Ejercicio 16
La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

Ejercicio 17
Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.

Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.

Ejemplo:

Introduzca número del dado: 5
En la cara opuesta está el "dos".
Ejercicio 18
Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

Ejercicio 19
Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

Ejercicio 20
Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

ZonaUbicaciónCosto/gramo1América del Norte24.00 euros2América Central20.00 euros3América del Sur21.00 euros4Europa10.00 euros5Asia18.00 euros

Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad.
Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

'''
