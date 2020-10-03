'''
## Funciones:

Es un conjunto de datos agrupados que funcionan realizando una tarea específica.
También son conocidas como métodos
'''

def Mayornumeros(a,b):

    if (a > b):
        print("El mayor valor es {} .".format(a))
    elif (b > a):
        print("El Mayor Valor es {}".format(b))
    else:
        print("Los valores son Iguales a = {} y b = {}".format(a,b))


while(True):
    try:
        a = int(input("Ingresa el primer valor...."))
        break
    except:
        print("El valor de A debe de ser entero y númerico...")

while (True):
    try:
        b = int(input("Ingresa el Segundo Valor...."))
        break
    except:
        print("El valor de B debe de ser entero y númerico...")

Mayornumeros(a,b)
