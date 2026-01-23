# TUPLAS

# Colecciones ordenadas e inmutables que permiten elementos duplicados, admiten tipos mixtos y se pueden desempaquetar, concatenar, multiplicar e iterar. 
# No se pueden modificar, pero si se pueden eliminar y agregar elementos.

# Se pueden crear con paréntesis o sin ellos.
# Se pueden crear con la función tuple().
# Se pueden crear con la función list() y luego con la función tuple().
# Se pueden crear con la función set() y luego con la función tuple().
# Se pueden crear con la función dict() y luego con la función tuple().
# Se pueden crear con la función range() y luego con la función tuple().
# Se pueden crear con la función enumerate() y luego con la función tuple().
# Se pueden crear con la función zip() y luego con la función tuple().
# Se pueden crear con la función map() y luego con la función tuple().
# Se pueden crear con la función filter() y luego con la función tuple().
# Se pueden crear con la función sorted() y luego con la función tuple().
# Se pueden crear con la función reversed() y luego con la función tuple().
# Se pueden crear con la función any() y luego con la función tuple().
# Se pueden crear con la función all() y luego con la función tuple().
# Se pueden crear con la función sum() y luego con la función tuple().
# Se pueden crear con la función max() y luego con la función tuple().
# Se pueden crear con la función min() y luego con la función tuple().

# Ejemplo de tupla

# Indice          0           1          2
tecnologias = ("Python", "JavaScript", "Go")

print(tecnologias) # ('Python', 'JavaScript', 'Go')

print("\n")

print(tecnologias[1]) # 'JavaScript'

# Puede tener elementos duplicados
tecnologias = ("Python", "JavaScript", "Go", "Python")

print("\n")

print(tecnologias) # ('Python', 'JavaScript', 'Go', 'Python')

print("\n")

print(len(tecnologias)) # 4)

print("\n")

# Tupla de un solo elemento

print(type(tecnologias)) # <class 'tuple'>

fruta = ("manzana")

print("\n")

print(type(fruta)) # <class 'str'>

tecnologias = ("Python",) # Debe ponerse una coma al final para que sea una tupla.

print("\n")

print(tecnologias) # ('Python',)

# Puede tener distintos tipos de datos.

tupla = ("Python", 1, True, 1.5)
print("\n")
print(tupla) # ('Python', 1, True, 1.5)
print("\n")

# DESEMPAQUETAR una colección.

tupla = ("Python", 1, True)

print(tupla) # ('Python', 1, True)

x, y, z = tupla

print(x) # Python
print(y) # 1
print(z) # True

# CONCATENAR tuplas con +.

tupla1 = (1,2,3)
tupla2 = (3,4,5)

tupla3 = tupla1 + tupla2
print("\n")
print(tupla3) # (1, 2, 3, 3, 4, 5) Se púede repetir el 3.


# MULTIPLICAR tuplas con *.

print("\n")
print(tupla1 * 2) # (1, 2, 3, 1, 2, 3)

# BUCLE FOR con tuplas

print("\n")

for item in tupla1:
    print(item) # Se imprime cada elemento de la tupla.

print("\n")

# TRUCO: Insertar un elemento en una tupla.

print("Truco para insertar un elemento en una tupla")

tupla1 = (1,2,3)
print("\n")
print(tupla1) # (1, 2, 3)

tupla1 = list(tupla1)
print("\n")
print(tupla1) # [1, 2, 3]

tupla1.append(4)
print("\n")
print(tupla1) # [1, 2, 3, 4]

tupla1 = tuple(tupla1) # Con tuple logramos convertir la lista en una tupla.
print("\n")
print(tupla1) # (1, 2, 3, 4)



# TRUCO: Eliminar una tupla.
print("\n")
print("Truco para eliminar una tupla")

del tupla1

print("\n")

# print(tupla1) # NameError: name 'tupla1' is not defined

