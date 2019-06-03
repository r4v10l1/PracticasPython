example = [1, "helloworld", True, 12.34, [1, 2, 3, 4]]
colores = ["Red", "Green", "Blue"]

number_list = list((1, 2, 3, 4, 5))
print (number_list)

rango = list(range(1, 100)) #todos los numeros entre 2 que especifiquemos
print (rango)

print (len(example)) #numero de elementos de la lista
print (colores[2]) #blue PORQUE EL PRIMERO ES 0

print ("Green" in colores) #con esto se "pregunta" si green está en la variable colores
print ("violet" in colores) # los 2 responden con un booleano
# ojo a las mayusculas

print (colores)
colores[0] = "Yellow"
print (colores)

colores.append("Violet")
##colores.append(("Black", "White")) 
# Para añadir un elemento a la lista
# Se ponen 2 paréntesis porque el comando solo acepta 1 elemento, y con la tupla,
# lo interpreta como 1. 
##print (colores)
# PERO, en la lista se muestra como
# ['Yellow', 'Green', 'Blue', 'Violet', ('Black', 'White')]
# Con  los paréntesis. Para evitar esto, se usa otro comando.
colores.extend(("Black", "White"))
# Este tampoco podrá utilizar más de 1 elemento, asi que se tiene que poner
# en una lista o tupla también, solo que no mostrará los paréntesis / corchetes.
print (colores)

colores.insert(1, "Texto en posición 1")
# Con insert se instera UN elemento en la posición 1
##colores.insert(3, ("Pink", "Grey"))
# En este caso con parentesis porque no hemos usado el colores.extend
##print (colores)
colores.insert(len(colores), "Yo que coño sé")
# Utilizas el dato de la longitud del texto para determinar la posición
print (colores)
colores.pop()
# Elimina el último.
print (colores)
colores.remove("Green")
#Elimina el valor de la lista que le especifiquemos
print (colores)
colores.pop(1)
# Elimina el elemento de la posición 1, teniendo en cuenta la 0
# Si al colores.pop no se le especifica nada: (), eliminará el ultimo de la lista
print (colores)
##colores.clear()
# Elimina TODOS los elementos de la lista, dejándola vacia
##print (colores)
colores.sort()
# Ordena los colores. De manera alfabética si no se le especifica nada.
print (colores)
colores.sort(reverse=True)
# Se especifica que queremos que ordene la lista en orden alfabético inverso,
# se le especifica con un booleano.
print (colores)
print (colores.index("Blue"))
# Imprime la posición de el elemento de la lista que le especifiquemos.
# Contando con el 0
print (colores.count("Black"))
# Cuenta la cantidad de veces que aparece en la lista lo que le digamos.


