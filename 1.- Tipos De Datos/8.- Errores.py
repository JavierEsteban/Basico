'''
Sentencias Basicas :
Try
except
finallly
'''

## Declaración de una Tupla

frutas = (1, 2, ["Javier", "Roy"])

try:
    frutas.append('Jabu')
except:
    print("No se puede editar una tupla es inmutable : {}".format(frutas))
