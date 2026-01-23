# Conjunto o Set
# Un conjunto es una colección no ordenada y sin duplicados. 
# Es ideal para asegurar unicidad y realizar operaciones de teoría de conjuntos.
# Si se pueden modificar elementos, pero no se puede modificar un elemento en específico,
# sino que se debe eliminar y luego agregar el nuevo elemento.

frutas = {"manzana", "naranja", "mandarina", "naranja"}

print(frutas) # No imprime duplicados. 

print("\n")

print(type(frutas)) # <class 'set'> Set es conjunto en inglés.

print("\n")

print(len(frutas)) # Da 3 porque no imprime el duplicado. 

print("\n")

conjuntos = {"Python", 156, True} # Acepta distintos tipos de datos. 

print(conjuntos)

print("\n")

print(type(conjuntos)) # <class 'set'>

print("\n")

# Recorrer un conjunto
for item in frutas:
    print(item)  # Puede salir en cualquier orden.

print("\n")    

for item in conjuntos:
    print(item)  # Puede salir en cualquier orden.

# Validar si está en el conjunto.
print("\n")  
print("manzana" in frutas)  # True

print("\n")  
print("pera" not in frutas)  # True

# Agregar elementos a un conjunto

# Usando add()

frutas.add("pera")
print("\n")
print(frutas)  # {'manzana', 'naranja', 'mandarina', 'pera'}

# Usando update() para agregar múltiples elementos.
# update() acepta listas, tuplas, conjuntos u otros iterables.
frutas.update(["kiwi", "sandía"])

print("\n")
print(frutas)  # {'manzana', 'naranja', 'mandarina', 'pera', 'kiwi', 'sandía'}

# Otra opción para agregar elementos:
frutas_tropicales = {"piña", "mango"}
frutas.update(frutas_tropicales)  # también funciona con listas o tuplas

print("\n")
print(frutas)  # {'manzana', 'naranja', 'mandarina', 'pera', 'kiwi', 'sandía', 'piña', 'mango'}

# Eliminar elementos de un conjunto
# Usando remove(). Lanza un error si el elemento no existe.
frutas.remove("kiwi") # Elimina kiwi

print("\n")
print(frutas) # {'manzana', 'naranja', 'mandarina', 'pera', 'sandía', 'piña', 'mango'}

# Usando discard(). No lanza error si el elemento no existe.
frutas.discard("kiwi") # No lanza error aunque kiwi ya no esté.

print("\n")
print(frutas) # {'manzana', 'naranja', 'mandarina', 'pera', 'sandía', 'piña', 'mango'}

# frutas.remove("kiwi") # Elimina kiwi
# print("\n")
# print(frutas) # Lanza error porque kiwi ya no está.

frutas.discard("manzana") # No lanza error aunque kiwi ya no esté.

print("\n")
print(frutas) # {'naranja', 'mandarina', 'pera', 'sandía', 'piña', 'mango'}

# Usando pop(). Elimina un elemento aleatorio y lo retorna.
elemento_eliminado = frutas.pop()
print("\n")
print("Elemento eliminado:", elemento_eliminado)
print("Conjunto después de pop():", frutas)

# Usando clear() para vaciar el conjunto.
frutas.clear()
print("\n")
print(frutas)  # set() conjunto vacío

print("\n")
print("-----------------------------")
print("OPERACIONES DE TEORÍA DE CONJUNTOS")
print("-----------------------------")

print("\n")

A = {"A", "B", "C"}
B = {"C", "D", "E"}

C_union = A.union(B)             # {'A', 'B', 'C', 'D', 'E'}
I_inter = A.intersection(B)      # {'C'}
D_diff  = A.difference(B)        # {'A', 'B'} Son los elementos que están en A pero no en B.

print(C_union)
print(I_inter)
print(D_diff)

# ¿Cómo eliminar duplicados con sets desde listas o tuplas?

print("\n")

numeros = [1, 2, 2, 3, 3, 3]
unicos = list(set(numeros))
print(unicos)  # [1, 2, 3] (el orden puede variar)