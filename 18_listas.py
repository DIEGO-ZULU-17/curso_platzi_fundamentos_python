# LISTAS

# Las listas son colecciones almacenadas en una sola variable. 
# Son ordenadas, mutables y permiten duplicados. 
# Esto habilita operaciones de actualización y acceso preciso por posición sin perder el orden original.


# Índices:    0         1           2
frutas = ["manzana", "naranja", "mandarina"]

print("\n")

print("Imprime la lista")
print(frutas) # Imprime la lista

print("\n")

print(type(frutas)) # Imprime el tipo de dato de la lista: <class 'list'>

print("\n")

print(len(frutas)) # Imprime la cantidad de elementos de la lista

print("\n")

print(frutas[1]) # Imprime el elemento en la posición 1

print("\n")

frutas[1] = "limón" # Cambia el elemento en la posición 1

print("\n")

print(frutas) # Imprime la lista actualizada

print("\n")

print(frutas[-1]) # Imprime el último elemento de la lista

print("\n")

print(frutas[1:3]) # Imprime los elementos de la posición 1 a la 2

print("\n")

print(frutas[:2]) # Imprime los elementos de la posición 0 a la 1

print("\n")

print(frutas[1:]) # Imprime los elementos de la posición 1 a la última

print("\n")

frutas.append("pera") # Agrega un elemento al final de la lista
print(frutas) # Imprime la lista actualizada

print("\n")

frutas.insert(1, "banana") # Agrega un elemento en la posición 1
print(frutas) # Imprime la lista actualizada

print("\n")

frutas.remove("banana") # Elimina el elemento "banana" de la lista
print(frutas) # Imprime la lista actualizada

print("\n")

frutas.pop() # Elimina el último elemento de la lista
print(frutas) # Imprime la lista actualizada

print("\n")

frutas.pop(1) # Elimina el elemento en la posición 1
print(frutas) # Imprime la lista actualizada

print("\n")

del frutas[1] # Elimina el elemento en la posición 1
print(frutas) # Imprime la lista actualizada

print("\n")

frutas.clear() # Elimina todos los elementos de la lista
print(frutas) # Imprime la lista vacía

print("\n")

# Copiar una lista
frutas = ["manzana", "naranja", "mandarina"]
frutas_copia = frutas.copy()
print(frutas_copia) # Imprime la lista copiada

print("\n")

# La lista muestra valores duplicados

# Índices:    0         1           2            3
frutas = ["manzana", "naranja", "mandarina", "naranja"]

print(frutas) # Imprime la lista original con naranja duplicada

print("\n")

print(frutas.count("naranja")) # Imprime la cantidad de veces que aparece "naranja" en la lista

print("\n")

# En la lista se pueden mezclar tipos de datos
frutas = ["manzana", "naranja", "mandarina", 1, 2, 3, True, False]

print(frutas) # Imprime la lista con tipos de datos mezclados

print("\n")

print(type(frutas)) # Sigue siendo <class 'list'>.

print("\n")

print("Saber si un elemento está en la lista: ")

if "manzana" in frutas:
    print("Sí, la manzana está en la lista") # Imprime "Sí, está en la lista"

    print("\n")

### ¿Cómo agregar, eliminar y ordenar elementos?

# índice:      0        1       2
vehiculos = ["auto", "moto", "avión"]
print(vehiculos)

# Métodos:

'''
- append agrega al final.
- insert(i, x) agrega en el índice i.
- remove(x) borra la primera coincidencia del valor.
- pop(i) quita por índice y devuelve el elemento.
- sort() ordena en forma alfabética por defecto.
- reverse() invierte el orden actual.
'''
print("\n")

vehiculos.append("barco") # Agrega al final barco. Es el índice 3.
print(vehiculos)

print("\n")

vehiculos.insert(1, "bicicleta") # Agrega en el índice 1 bicicleta.
print(vehiculos)

print("\n")

vehiculos.remove("auto") # Elimina el primer elemento que coincida con "auto".
print(vehiculos)

print("\n")

vehiculos.pop(1) # Elimina el elemento del índice 1 y lo devuelve.
print(vehiculos)

print("\n")

vehiculos.sort() # Ordena alfabéticamente.
print(vehiculos)

print("\n")

vehiculos.reverse() # Invierte el orden actual.
print(vehiculos)

print("\n")

### UNIR LISTAS

# La diferencia: + crea una nueva lista; extend modifica la existente.

coleccion1 = [1, 2, 3]
coleccion2 = [4, 5, 6]

coleccion3 = coleccion1 + coleccion2
print(coleccion3) # [1, 2, 3, 4, 5, 6]
print(coleccion1) # [1, 2, 3] (no se modificó)
print(coleccion2) # [4, 5, 6] (no se modificó)
print("\n")

coleccion1.extend(coleccion2)
print(coleccion1) # [1, 2, 3, 4, 5, 6] (se modificó)
print(coleccion2) # [4, 5, 6] (no se modificó)