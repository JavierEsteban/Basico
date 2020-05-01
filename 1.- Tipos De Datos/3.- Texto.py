Cadena = "Hola Mundo"

Valor = Cadena[:2]
print(Valor)

#Funciones de Cadenas:

Cadena1 = "Hola Javier"
print(len(Cadena1))
print(Cadena1.upper())
print(Cadena1.lower())

Cadena2 = "Hola Javier Como Estas El día de Hoy"
print(Cadena2.split())

Cadena3 = "Uva,Platano,Pera,Sandia"
print(Cadena3.split(','))

#imprimir valores em cadena.

nombre = "Javier"
print("Buenos días " + nombre)

#.format
print("Buenos días {}".format(nombre))

resultado =10 / 3
print("El resultado es {r}".format(r = resultado))
print("El resultaod es {r:1.4f}".format(r= resultado))


'''
Ejemplo busqueda de palabras en un texto.
'''

def busca_palabra(palbra, texto):
    if palabra in texto:
        posicion = texto.find(palabra)
        largo = len(palabra)
        print("La palabra {} si exite y se encuentran en la posiciòn inicial de {} y final de {}".format(palabra,
                                                                                                         posicion,
                                                                                                         posicion + largo - 1))
    else:
        print("En el texto no se encuentra la palabra {}".format(palabra))

palabra = str(input("ingresa la palabra a Buscar : "))
texto = str(input("Ingresa el testo para la busqueda: "))

try:
    busca_palabra(palabra, texto)
except:
    print("No existe la palabra")
