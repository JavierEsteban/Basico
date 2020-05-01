
## Las sentencias de control en Python son los siguientes

'''
if ->  Condición basica
elif -> si no si
else -> si no
while -> iteración iterativa hasta encontrar un false
for -> recorrido de una lista.
'''

numero = str(input("Ingresa Comando: "))

if numero == 'Ingresar':
    print("bienvenido")
elif numero == 'Salir':
    print("Esta saliendo del sistema")
else:
    print("Nose reconoce")


## While

##con break
c = 0
while c < 7:
    c += 1
    if (c == 4):
        print("La iteración de c vale {}".format(c))
        break
    else:
        print("C es el valor {}".format(c))

print("La iteración termino el valor final de c es {}".format(c))


##con continue
c = 0
while c < 7:
    c += 1
    if(c == 4):
        #print("La iteración de c vale {}".format(c))
        continue
    else: print("C es el valor {}".format(c))



print("La iteración termino el valor final de c es {}".format(c))


## Ejemplo Práctico con while

while(True):
    opcion = str(input(""""
    Ingresar que tipo de operacion quiere realizar ?
    1.- Saludos
    2.- Suma
    3.- Salir
    """))

    if (opcion == '1'):
        nombre = str(input("Ingresar Su Nombre : "))
        print("Hola {}, Bienvenido al sistema.".format(nombre))
    elif (opcion == '2'):
        numero = int(input("ingresar el Primer número: "))
        numero_2 = int(input("Ingresar el segundo Núemro: "))
        suma = numero + numero_2
        print("La suma de los número es {}".format(suma))
    elif(opcion == '3'):
        print("Saliendo del Sistema....")
        break
    else:
        print("Ingresaron un comando no conocido, vuelva a intentarlo")


### For

numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0

while(indice < len(numeros)):
    print(numeros[indice])
    indice += 1


for numero in numeros:
    print(numero)


##ejemplo:
lista = [1,2,3,4,5,6,7,8,9,10]
indice = 0

for numero in lista:
    lista[indice] *= 10
    indice += 1

print(lista)

##Ejemplo con Enumerate
lista = [1,2,3,4,5,6,7,8,9,10]

for indice, numero in enumerate(lista):
    lista[indice] *= 10
print(lista)
