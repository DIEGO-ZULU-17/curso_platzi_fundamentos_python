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



