# BUCLE FOR

# Ejemplo con una palabra
palabra = "Python"

for letra in palabra:
    print(letra) # Imprime cada letra P, y, t, h, o, n

print("\n")


# Ejemplo con una lista
frutas = ["Manzana", "Naranja", "Kiwi"]

for fruta in frutas:
    print(fruta) # Imprime cada fruta Manzana, Naranja, Kiwi
    if fruta == "Naranja":
        print("Naranja es mi fruta favorita")

print("\n")


# break finaliza el bucle
for fruta in frutas:
    if fruta == "Naranja":
        break
    print(fruta) # Solo imprime Manzana porque cuando encuentra Naranja el bucle se rompe.

print("\n")

# continue salta a la siguiente iteracion
for fruta in frutas:
    if fruta == "Naranja":
        continue
    print(fruta) # Imprime Manzana y Kiwi porque cuando encuentra Naranja salta a la siguiente iteracion.

print("\n")

# else se ejecuta cuando el bucle finaliza sin encontrar un break
for fruta in frutas:
    if fruta == "Naranja":
        continue
    print(fruta) # Imprime Manzana y Kiwi porque cuando encuentra Naranja salta a la siguiente iteracion.
else:
    print("El bucle ha finalizado sin encontrar un break")
    print("Ya hemos terminado el bucle for")

print("\n")


# range: consiste en generar una secuencia de numeros. 
print("Uso de range\n")

# range con fin: comienza en el cero y termina en el numero que le pasemos menos uno.
for i in range(10):
    print(i) # Imprime del 0 al 9

print("\n")

# range con inicio y fin: comienza en el numero que le pasemos y termina en el numero que le pasemos menos uno.
for i in range(5, 10):
    print(i) # Imprime del 5 al 9

print("\n")

# range con inicio, fin y paso: comienza en el numero que le pasemos, termina en el numero que le pasemos menos uno y avanza de 2 en 2. El paso se encarga de decirle al bucle que avance de 2 en 2.
for i in range(0, 10, 2):
    print(i) # Imprime del 0 al 9 de 2 en 2

print("\n")

for i in range(0, 11, 2): # Coloca 11 para que incluya el 10.
    print(i) # Imprime del 0 al 10 de 2 en 2

print("\n")

# range con inicio, fin y paso negativo
for i in range(10, 0, -1):
    print(i) # Imprime del 10 al 1

print("\n")

# range con inicio, fin

# Bucle anidado

print("Bucle anidado\n")

frutas = ["Manzana", "Naranja", "Kiwi"]
adjetivos = ["rica", "saludable"]

for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo) # Primero revisa el primer bucle y luego el segundo bucle.
# manzana rica
# naranja rica
# kiwi rica
# manzana saludable
# naranja saludable
# kiwi saludable

print("\n")

# Desafío propuesto: lograr el orden manzana rica, manzana saludable, naranja rica, naranja saludable, kiwi rica, kiwi saludable.
for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta, adjetivo)

print("\n")

# Uso de pass
# Se usa pass para que no se ejecute el bucle y no se muestre nada.

print("Uso de pass\n")

for fruta in frutas:
    pass # No se ejecuta el bucle y no se muestra nada.

