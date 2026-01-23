# Operadores de comparación

x = 5
y = 3
z = 5

print(x == y) # Si es igual: False
print(x != y) # Si es distinto: True
print(x > y) # Es mayor a la segunda: True
print(x < y) # Es menor a la segunda: False
print(x >= y) # Es mayor o igual a la segunda: True
print(x >= z) # Es mayor o igual a la segunda: True
print(x <= z) # Es menor o igual a la segunda: True
print(x <= y) # Es menor o igual a la segunda: False

# Operadores lógicos

print(x > y and y > z) # and = Ambas se deben cumplir para que el resultado sea True. Primera condición es True, segunda False. El resultado es False.

print(x > y or y > z) # or = Alguna se debe cumplir para que el resultado sea True. Con que una sea True, el resultado es True.

print(x == y or y > z) # Primera condición es False, segunda es False. El resultado es False.

# La negación = not

v = True
f = False

print(not v) # Imprime False porque v es True.
print(not f) # Imprime True porque f es False.

