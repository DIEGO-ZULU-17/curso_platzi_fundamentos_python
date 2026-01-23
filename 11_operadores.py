# Operadores aritméticos

x = 5
y = 10

# Suma
print(10 + 10) # 20
print("Suma", x + y) # Suma 15

# Resta
print(10 - 5) # 5
print("Resta", x - y) # Resta -5

# Multiplicación
print(10 * 2) # 20
print("Multiplicación", x * y) # Multiplicación 50

# División / (retorna un float)
print(10 / 2) # 5.0
print("División", y / x) # División 2.0

# Módulo % (el resto de la división)
print(10 % 2) # 0
print("Módulo (resto)", y % x) # Módulo 0
x1 = 5
y1 = 12
print("Módulo (resto)", y1 % x1) # Módulo 2

# Potencia **
print(10 ** 2) # 100
print("Potencia", y ** x) # Potencia es 10 * 10 * 10 * 10 * 10 = 100000

# División entera //
print(10 // 3) # 3
print("División entera", y // x) # División entera 2
x1 = 5
y1 = 12
print("División entera", y1 // x1) # División entera 2 (sin la parte decimal)

# Cuando usar módulo: calcular un número par
par = 8
print("El número", par, "es par: ", par % 2 == 0) # True
par1 = 9
print("El número", par1, "es par: ", par1 % 2 == 0) # False

# Preferencia de Operadores
# 1. Parentesis
# 2. Potencia
# 3. Multiplicación, división, división entera y módulo
# 4. Suma y resta
# 5. Comparaciones de identidad y pertenencia
# 6. Comparaciones de igualdad y desigualdad
# 7. Operadores lógicos (not, and, or)
# 8. Operadores de asignación


# Operadores de comparación

# Igualdad
print(10 == 10)

# Desigualdad
print(10 != 10)

# Mayor que
print(10 > 5)

# Menor que
print(10 < 5)

# Mayor o igual que
print(10 >= 10)

# Menor o igual que
print(10 <= 5)


# Operadores lógicos

# AND
print(True and True)

# OR
print(True or False)

# NOT
print(not True)


# Operadores de asignación

# Asignación
x = 10

# Suma y asignación
x += 5 # x = x + 5

# Resta y asignación
x -= 3 # x = x - 3

# Multiplicación y asignación
x *= 2 # x = x * 2

# División y asignación
x /= 4 # x = x / 4

# Módulo y asignación
x %= 3 # x = x % 3

# Potencia y asignación
x **= 2 # x = x ** 2

# División entera y asignación
x //= 3 # x = x // 3


# Operadores de identidad

# is
x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)  # False

# is not
print(x is not y)  # True


# Operadores de pertenencia

# in
print(1 in x)  # True

# not in
print(4 not in x)  # True