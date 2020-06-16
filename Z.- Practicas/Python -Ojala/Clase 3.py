# Manejo de archivos con python

def Escritura_Archivo(valor = "Defecto"):
    archivo = open("archivo.txt","w+")
    for i in range(0,6):
        archivo.write("El valor ingresado es {} y está es la corrida {} ..\n".format(valor,i+1))

def main():
    Valor = str(input("Ingrese el valor que desee que salga..."))
    Escritura_Archivo(Valor)
    print("ProgramaFinalizado.....")

    pass

if __name__ == '__main__':
    main()


"""
# Open a file in read/write mode
fo = open("archivo.txt", "r+")
print("Name of the file: ", fo.name)




# Open a file
fo = open("archivo.txt", "r")
print ("Name of the file: ", fo.name)

# Close opened file
fo.close()

"""
