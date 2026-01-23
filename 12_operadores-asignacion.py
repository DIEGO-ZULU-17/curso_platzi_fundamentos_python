# Operadores de Asignación

x = 5

# Suma

x = x + 3 # 8

print(x)

x += 3 # 11 porque x ya valía 8

print(x)

# Resta

x -= 3 # 8 porque x valía 11

print(x)

# Multiplicación
x *= 3 # 24 porque x valía 8

print(x)

# División
x /= 3 # 8.0 porque x valía 24. El resultado es tipo float.

print(x)

# Módulo
x %= 3 # 2.0 porque x valía 8.0. El resultado es tipo float porque la / era tipo float.

print(x)

# División entera
y = 20
y //= 2 # 10 porque y valía 20. El resultado es tipo int.

print(y)

# Potencia o Exponente
y **= 3 # 10x10x10 = 1000 porque y valía 10. 

print(y)

# Operador WALRUS (morsa) := (El signo parece una morsa)
# Aplica desde Python 3.8

print(z := 3) # Imprime 3 y asigna 3 a z.
print(z) # Imprime 3 porque z ya valía 3.


