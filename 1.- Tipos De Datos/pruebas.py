

def calculo_media():
    cantidad_veces = int(input("ingresar la cantidad de números A ANALIZAR: "))
    conteo = 0
    Sumatotal = 0

    while(conteo < cantidad_veces ):
        numero = int(input("Ingrese el número a evaluar : "))
        Sumatotal = numero + Sumatotal
        conteo = conteo + 1

    Media = Sumatotal / cantidad_veces
    print ("La media de los valores es : {}".format(Media))


while(0==0):
    Pregunta = str(input("Presione S/N si desea realiza el calculo de la Media}:"))
    if(Pregunta=='S'):
       calculo_media()
    else:
        break
