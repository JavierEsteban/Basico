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
print("Buenos días ".format(nombre))

resultado =10 / 3
print("El resultado es {r}".format(r = resultado))
print("El resultaod es {r:1.4f}".format(r= resultado))
