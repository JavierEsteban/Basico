## Tipos de Datos En python
'''
 Los tipos de datos más básicos:
 1.- Números
 2.- String
 3.- Complejos

'''
# Numeros
numerico = 1
print(type(numerico))

decimal = 2.2
print(type(decimal))


#String
Cadena = "Javier"
print(type(Cadena))

Cadena2 = 'Javier'
print(type(Cadena2))


#Operadores
Suma = numerico + decimal
print(Suma)

Concatenacion = Cadena + ' ' + Cadena2
print(Concatenacion)

Division = 12 / 5
print(Division)

#### Metodos de los tipos de Datos
dir(Cadena)
dir(numerico)
dir(decimal)



## Caracteres Especiales...

# \n  -->  Salto de línea
# \t  -->  Salto de Tabulación

Cadena3 = "Esto es una \ncadena"
print(Cadena3)


Cadena4 = "Esto es una \tcadena"
print(Cadena4)

Cadena5 = r"C:\nombre\directorio"
print(Cadena5)

diez_espacios = 'a' + ' '*10 + 'b'
print(diez_espacios)

cadena6 = 'Python'
print(cadena6[0])
print(len(cadena6))

print(cadena6[2:])

contador = 0
while (contador < len(cadena6)):
    print(cadena6[contador])
    contador = contador + 1

# Operadores Logicos
#(and, or, not)
print (True == 1)

Nombre = 'Javier'
Edad = 26


print(Edad < 27 and Nombre[0] == 'J')


print(Edad < 27 and Nombre[0] == 'J')
print(Edad < 27 or Nombre[0] == 'J')

print( not (Edad < 27))

Cadena5 = 'zeréP nauJ, 01'

cadena6 = Cadena5[::-1]

print(cadena6[4:] + ' ha sacado una Nota de ' + cadena6[:2])
