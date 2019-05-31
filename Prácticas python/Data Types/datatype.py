
# Strings
print ()
print("[ STRINGS ]")
print ("[=========================]")
print ("hello world")
print ("HELLO WORLD")
print ('hello world (solo una comilla)')
print (type ("hello world"))
print ()
print ()

# Numbers
print ("[ NUMBERS ]")
print ("[=========================]")
# Integer (entero)
print ("Integer")
print (666)
print (type (666))
# Float (con decimal)
print ("Float")
print (6.66)
print (type (6.66))
print ()
print ()

# Boolean (booleano)
print ("[ BOOLEANS ]")
print ("[=========================]")
print (True)
print (type (True))
print ()
print ()

# List (listas)
print ("[ LIST ]")
print ("[=========================]")
# Solo Integers
print ([10, 20, 30, 312342452])
# Solo strings
print (["hola", "HOLA", "hola mundo", "sdfsfsagfgeargdfgerg"])
# Integer, String, Booleano y Float
print ([666, "Hello", True, 6.66])
print (type([1.75, "Texto String"]))
print ()
print ()

# Tuples
# (Son como las listas, solo que a lo largo del programa, 
# los datos que contiene no se pueden modificar.)
# Se escriben entre paréntesis, no corchetes.
print ("[ TUPLES ]")
print ("[=========================]")
print ((1, 2, 3, 14131))
print (type((1, 12313)))
print ()
print ()

# Dictionaries (diccionarios)
print ("[ DICTIONARIES ]")
print ("[=========================]")
print ({
    "Nombrepersona":"José Juan Luis Jacobo",
    "Apellido":"de Jerusalén",
    "Apodo":"xX_comunistautista777_Xx",
    "Número de cuenta >:D":123456789
    })
print (type({
    "Nombrepersona":"José Juan Luis Jacobo",
    "Apellido":"de Jerusalén",
    "Apodo":"xX_comunistautista777_Xx",
    "Número de cuenta >:D":123456789
    }))
print ()

# Es un conjunto de datos definidos por una clave (key)
# Explicación en https://devcode.la/tutoriales/diccionarios-en-python/
# Por ejemplo:

diccionario1 = {
    "Nombre":"Luis",
    "Apellido":"de la Mancha",
    "Username":"NoTengoVida01",
    "Password":123456789,
    #También se pueden listas
    "Mascotas":["Perro", "Gato"]
    }

print (diccionario1["Nombre"]) #Luis
print (diccionario1["Apellido"]) #de la Mancha
print (diccionario1["Password"]) #123456789
print (diccionario1["Mascotas"]) #Perro Gato
# Se pueden seleccionar elementos especificos
# de las listas de los diccionarios
print (diccionario1["Mascotas"][0]) #Perro
print (diccionario1["Mascotas"][1]) #Gato

print ()
print ()

# None (dato vacio)
print ("[ NONE ]")
print ("[=========================]")
print (None)
print (type(None))
