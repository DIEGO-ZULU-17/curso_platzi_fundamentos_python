# Texto (strings) en Python

comillasSimples = 'Este es un texto con comillas simples'
comillasDobles = "Este es un texto con comillas dobles"
comillasTriplesSimples = '''Este es un texto con comillas triples simples'''
comillasTriplesDobles = """Este es un texto con comillas triples dobles"""

print(comillasSimples)
print(comillasDobles)
print(comillasTriplesSimples)
print(comillasTriplesDobles)

# Números en Python

a = 1
b = 3.14 # Utiliza punto para los decimales
c = 5 + 2j # Número complejo, usa j para la parte imaginaria    

print(a)
print(b)
print(c)

# Lista: si se puede modificar su contenido.

lista = [0,1,2,3,4,5] # Usa [] para definir listas
print(lista)

# Tuplas: no se puede modificar su contenido.

tupla = (0,1,2,3,4,5) # Usa () para definir tuplas
tupla2 = 0,1,2,3,4,5 # También puedes definir tuplas sin paréntesis
tupla3 = ("a","b","c") # Tupla de strings
print(tupla)
print(tupla2)
print(tupla3)

'''
Algo a tener en cuenta con las tuplas es que la referencia no es mutable, pero su contenido si.

Por ejemplo, no se puede modificar una tupla si los tipos de datos son números o strings: tupla = (1,2,3) o del tipo tupla = ("1", "2", "3")

Sin embargo, el contenido de una lista dentro de una tupla si puede ser modificado:

tupla = ([1,2,3])

Lo mismo sucede con los diccionarios.

tupla[0].append(4)

Va a resultar en tupla = ([1,2,3,4])

Si necesitas guardar un conjunto de datos que no cambiarán, ¿qué tipo de estructura usarías?
- Tupla

'''

# Diccionarios: pares clave-valor. Si se puede modificar su contenido.

diccionario = {"clave1": "valor1", "clave2": "valor2"} # Usa {} para definir diccionarios
print(diccionario)

diccionario2 = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print(diccionario2) # Se puede acceder a cada par clave-valor con los indices.

# En listas, tuplas y diccionarios se pueden mezclar diferentes tipos de datos y repetir los elementos.

# Conjuntos (sets): colección no ordenada de elementos únicos. Mutables.

conjunto = {1, 1, 2, 2, 3, 4, 5} # Usa {} para definir conjuntos
print(conjunto) # Imprime {1, 2, 3, 4, 5} ya que los elementos duplicados se eliminan

# Booleanos: True o False
booleanoVerdadero = True # Con T mayúscula
booleanoFalso = False # Con F mayúscula