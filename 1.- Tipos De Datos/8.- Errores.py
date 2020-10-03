'''
Sentencias Basicas :
Try
except
finallly

Controlar los errores, atraves de excepciones.

'''

### Errores en tiempo de ejecución Básicas.
## Declaración de una Tupla

frutas = (1, 2, ["Javier", "Roy"])

try:
    frutas.append('Jabu')
except:
    print("No se puede editar una tupla es inmutable : {}".format(frutas))

### Errores en TIEMPO DE EJECUCIÓN AVANZADAS..

try:
    n = float(input("Ingrese un número: "))
    10 / n
except  TypeError:
    print("No se puede dividir el número por una cadena..")
except ValueError:
    print("Debes de Ingresar un Número..")
except ZeroDivisionError:
    print("No se puede dividir entre cero..")
except Exception as e:
    print(type(e).__name__)
