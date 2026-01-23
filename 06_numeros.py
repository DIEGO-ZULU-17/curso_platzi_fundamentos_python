# Tipos de datos numéricos
import random

x = 1
y = 2.5
z = 3 + 4j

print (type(x)) # Imprime <class 'int'>)
print (type(y)) # Imprime <class 'float'>
print (type(z)) # Imprime <class 'complex'>

positivo = 5
negativo = -5
print(positivo)
print(negativo)

positivoFloat = 5.5
negativoFloat = -5.5
print(positivoFloat)
print(negativoFloat)

imaginario = 3 + 2j
imaginarioNegativo = -3 - 2j # Se pueden combinar todos los tipos de números y signos.
print(imaginario)
print(imaginarioNegativo)

# Casteo: convertir entre tipos de datos numéricos.

x = 1
y = 2.5

xf = float(x) # Convierte int a float
print(type(xf)) # Imprime <class 'float'>
print(xf) # Imprime 1.0

ye = int(y) # Convierte float a int (pierde la parte decimal)
print(type(ye)) # Imprime <class 'int'>
print(ye) # Imprime 2

# Se puede convertir un número a complejo, pero no viceversa.

entero = 5
flotante = 5.5

enteroComplejo = complex(entero)
flotanteComplejo = complex(flotante)

print(enteroComplejo) # Imprime (5+0j)
print(type(enteroComplejo)) # Imprime <class 'complex'>

print(flotanteComplejo) # Imprime (5.5+0j)

# Importación: Usa import random. 
print(random.randrange(1, 10)) # Imprime un número aleatorio entre 1 y 9. El 10 no está incluido.
