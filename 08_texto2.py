# indice: la primera posición es 0.
# Los espacios cuentan como posición.
from re import split


texto = "Este es un texto"

print(texto[0]) # E
print(texto[1]) # s
print(texto[2]) # t
print(texto[3]) # e
print(texto[4]) # (espacio)


# Si queremos acceder a un índice que no existe, nos dará un error.
# print(texto[100]) # IndexError

print(texto[0:4]) # Este (no incluye el caracter 4)
print(texto[5:9]) # es u (no incluye el caracter 9)
print(texto[10:16]) # texto (no incluye el caracter 16)

print(texto[0:10:2]) # Eee u

print(texto[::-1]) # otxet nu se etsE

print(texto[:7]) # Este es (Inicia en 0 y termina en el caracter 6)

print(texto[7:]) # un texto (Inicia en el caracter 7 y termina en el final)

print(texto[5:-2]) # es un tex (Inicia en el caracter 5 y termina en el caracter -2).


# Reemplazar, dividir y normalizar texto

curso = "Este curso es de Javascript"

print(curso.replace("Javascript", "Python")) # Este curso es de Python

curso = "Este curso es de Javascript, Javascript"

print(curso.replace("Javascript", "Python")) # Este curso es de Python, Python.

# Dividir texto por alguno de los caracteres

textoDividido = texto.split(" ")

print(textoDividido) # ['Este', 'es', 'un', 'texto']

# Normalización: Python es case sensitive
texto2 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"
print("mayusculas" in texto2) # False
print("MAYUSCULAS" in texto2) # True

print("mayusculas".lower() in texto2.lower()) # True: porque el texto2 se convierte en minusculas

texto3 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"
print(texto3.lower().count("mayusculas")) # 1
