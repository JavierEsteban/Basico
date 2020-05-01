# Estructura de Datos Python
'''
###############################
#########  Listas :  ##########
###############################
'''


###  Listas : Las listas son esructuras flexibles que puede tener varios tipos de datos... " SON MUTABLES.. "

lista_numeros = [1,2,3,4,5]
print(lista_numeros)

lista_textos = [1,'2',3,4,5]
print(lista_textos )

listas_totales = lista_numeros + lista_textos
print(listas_totales)

###  Metodos :
'''
    append() -> agrega un elemento al final de la lista.
    extend() -> agrega otra lista a la lista.
    
    count() ->  cuenta cuantos elementos se repiten en la lista.  
    index() ->  enumera el elemento de la posicion
    insert() -> inserta el elemnto en la posición.
    remove() -> elimina el elemnto en la posición.
    pop() ->  devuelve el último valor de la lista.
    sort() ->  ordenar la lista de elementos.
'''


listas_frutas = ['Manzanas', 'Peras','Platanos', 'Yucas']
listas_frutas.append('Mandarinas')   #append
listas_frutas2 = ['Melon', 'Papaya']
listas_frutas.extend(listas_frutas2)  #Extend()
print(listas_frutas)

listas_frutas.append('Manzanas')
print(listas_frutas.count('Manzanas'))

print(listas_frutas.index('Peras'))

listas_frutas.insert(4, 'Manzanas')
print(listas_frutas)


listas_frutas.remove( 'Yucas')
print(listas_frutas)


ejemplo_lista1 = list()
ejemplo_lista1.append('Melon')


ejemplo_lista1.extend(['Melon', 'Papaya'])

ejemplo_lista1

'naranjas' in ejemplo_lista1


###############################
#########  Tuplas :  ##########
###############################


###   Tuplas : Son un tipo de lista que tiene la caracteristica de ser inmutabe


#Declaración de la tupla
numeros = tuple()
print (type(numeros))

numeros_1 = (0,1,2,3)
print (type(numeros_1))



dictionario = { '1' : "Javier", '2' : "Roy"}

print(dictionario.keys())

