# Hago una variable llamada myStr (my String)
myStr = "Hello World"

# print (dir(myStr))
# Muestra las opciones posibles con myStr

print (myStr.upper())
# Convierte la varible en todo mayusculas
print (myStr.lower())
# Convierte la variable en todo minusculas
print (myStr.title())
# Le pone a todas las palabras del String la primera letra con mayúscula
print (myStr.swapcase())
# Cambia todas las mayúsculas del String a minusculas y viceversa
print (myStr.capitalize())
# Pone la primera letra del texto en mayúscula y el resto en minuscula
print (myStr.replace("Hello", "Bye"))
# Cambia ciertas palabras del String por otras
print (myStr.replace("Hello", "Bye").upper())
# Se pueden convinar entre ellos, por ejemplo intercambiando palabras
# y luego poniendolo en mayusculas.
print (myStr.count("l"))
# Cuenta las veces que aparece en el String la letra que le especifiquemos
print (myStr.count(" "))
# El espacio cuenta como 1 caracter y tambien puede ser contado
print (myStr.startswith("hola"))
# Podemos ver si la variable myStr empieza por esta palabra (esos caracteres)
# Utiliza los booleanos para decierme si empieza o no por esa palabra
print (myStr.endswith("World"))
# Comprueva si la palabra acaba o no por esa palabra
print (myStr.split())
# Separa el String en 2 basado en el espacio (o caracter especificado)
print (myStr.split("W"))
# Por ejemplo aqui separa por la W (y muestra el espacio al separarlo)
print (myStr.split("o"))
# O por la letra "o" (en 3 partes)
# Además, split Crea una lista con las distintas partes del String
print (myStr.find("W"))
# Muestra la POSICIÓN de la letra "W" (contando espacio)
# Empieza a contar por el 0 (la "H" seria el 0 y la "e" el 1)
print (len(myStr))
# Muestra la longitud del String (11) EMPEZANDO POR 0
print (myStr.index("e"))
# Parecido a find
print (myStr.isnumeric())
# Muestra si el String es numerico
print (myStr.isalpha())
# Muestra si el String es alfanumerico
# Ambos 2 en booleano
print (myStr[4])
# Imprime solo lo que está en la posición 4 ("o")
print (myStr[-2])
# Con menos (-) delante empieza a contar por el final del String
print ("Hola mundo es " + myStr)
# En un print se pueden sumar Strings y variables
print ("Hola mundo es {myStr}")
# En este caso se imprimairia tal cual Hola mundo es {myStr}
# Para que interprete {myStr} como la variable, tenemos que poner una [f] delante
print (f"Hola mundo es {myStr}")
# De esta manera
print ("Hola mundo es {0}".format(myStr))
# Con el format se le indica que en ese 0 va la variable myStr



# Si se quiere comentar un texto seleccionado, con [Ctrl] + [Mayusculas] + [P]
# se abre un menú en el que si se busca comment, se comenta lo seleccionado

