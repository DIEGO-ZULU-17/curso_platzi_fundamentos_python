# Una lambda es una función pequeña y anónima: no tiene nombre, puede recibir varios argumentos, pero contiene una sola expresión. 
# Es ideal para operaciones cortas donde definir una función completa sería más largo.

# Sintaxis básica: palabra clave, argumentos, dos puntos y expresión.

# lambda argumentos: expresión`

x = lambda a: a + 10 # La función lambda toma un argumento 'a' y devuelve 'a + 10'
print(x(5))  # Salida: 15

print("\n")

x = lambda a, b: a + b  # La función lambda toma dos argumentos 'a' y 'b' y devuelve su suma
print(x(3, 5))  # Salida: 8

def mi_función(n): # Definimos una función normal que devuelve una función lambda
    return lambda a: a * n # La función lambda toma un argumento 'a' y lo multiplica por 'n'

duplicador = mi_función(2) # Creamos una función que duplica el valor.
triplicador = mi_función(3) # Creamos una función que triplica el valor.

print("\n")
print(duplicador(5))  # Salida: 10
print("\n")
print(triplicador(5))  # Salida: 15

# Quintuplicador
quintuplicador = mi_función(5)
print("\n")
print(quintuplicador(5))  # Salida: 25

# Las funciones lambda son útiles en funciones de orden superior como map(), filter() y reduce().

numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x**2, numeros))  # Eleva al cuadrado cada número en la lista

print("\n")
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

pares = list(filter(lambda x: x % 2 == 0, numeros))  # Filtra los números pares de la lista

print("\n")
print(pares)  # Salida: [2, 4]

from functools import reduce

suma_total = reduce(lambda x, y: x + y, numeros)  # Suma todos los números en la lista

print("\n")
print(suma_total)  # Salida: 15

# Aunque las funciones lambda son poderosas, es importante no abusar de ellas.
# Si una función lambda se vuelve demasiado compleja, 
# es mejor definir una función normal para mejorar
# la legibilidad y el mantenimiento del código.

# Ejemplo de función lambda compleja (no recomendada)
compleja = lambda x: x**2 + 2*x + 1 if x > 0 else x**2 - 2*x + 1

print("\n")
print(compleja(3))  # Salida: 16 porque 3**2 + 2*3 + 1 = 9 + 6 + 1 = 16

print("\n")
print(compleja(-3))  # Salida: 16 porque (-3)**2 - 2*(-3) + 1 = 9 + 6 + 1 = 16

# En resumen, las funciones lambda son una herramienta útil para crear funciones pequeñas y rápidas en Python.
# Son especialmente útiles en combinación con funciones de orden superior.
# Sin embargo, siempre debemos considerar la claridad del código al decidir cuándo usarlas.

