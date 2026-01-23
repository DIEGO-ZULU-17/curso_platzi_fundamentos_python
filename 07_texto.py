# Formas de imprimir texto

print("Hola 'mundo'") # Imprime Hola 'mundo'
print('Hola "mundo"') # Imprime Hola "mundo"
print('''Hola "mundo"''') # Imprime Hola "mundo"
print("""Hola 'mundo'""") # Imprime Hola 'mundo'

print("Hola \"mundo\"") # Imprime Hola "mundo"
print('Hola \'mundo\'') # Imprime Hola 'mundo'

print("Hola \nmundo") # Imprime Hola
# mundo

print("Hola \tmundo") # Imprime Hola     mundo

print("Hola \\mundo") # Imprime Hola \mundo

print("Hola " + "mundo") # Imprime Hola mundo

# Para palabras en inglés, utiliza comillas simples para evitar problemas con las comillas dobles.
ingles = "I'm Diego" # Imprime I'm Diego
print(ingles)

multiples = """Hola
mundo
desde
las
comillas
triples"""
print(multiples) # Imprime Hola
# mundo

palabra = "Murcielago"
print(len(palabra)) # Imprime 10 porque tiene 10 caracteres

texto = "Este curso es de Fundamentos de Python"
estaIncluida = "Python" in texto
print(estaIncluida) # Imprime True

texto = "Este curso es de Fundamentos de Python"
estaIncluida = "python" in texto
print(estaIncluida) # Imprime False porque es case sensitive.

noEstaIncluida = "Javascript" not in texto
print(noEstaIncluida) # Imprime True

mayuscula = texto.upper() # Convierte todo el texto a mayúsculas
print(mayuscula) # Imprime ESTE CURSO ES DE FUNDAMENTOS DE PYTHON

minuscula = texto.lower() # Convierte todo el texto a minúsculas
print(minuscula) # Imprime este curso es de fundamentos de python

capitalize = texto.capitalize() # Convierte la primera letra a mayúscula
print(capitalize) # Imprime Este curso es de fundamentos de python

title = texto.title() # Convierte la primera letra de cada palabra a mayúscula
print(title) # Imprime Este Curso Es De Fundamentos De Python

swapcase = texto.swapcase() # Convierte las mayúsculas a minúsculas y viceversa
print(swapcase) # Imprime eSTE CURSO ES DE fUNDAMENTOS DE pYTHON

replace = texto.replace("Python", "JavaScript") # Reemplaza una palabra por otra
print(replace) # Imprime Este curso es de Fundamentos de JavaScript

split = texto.split(" ") # Divide el texto en una lista de palabras
print(split) # Im

# Eliminar espacios
espacios = "   Hola mundo   "
print(espacios.strip()) # Elimina los espacios en blanco al inicio y al final. Imprime Hola mundo
print(espacios.lstrip()) # Elimina los espacios en blanco al inicio. Imprime Hola mundo
print(espacios.rstrip()) # Elimina los espacios al final. Imprime "    Hola mundo"


