v = True
f = False

print(v) # True
print(f) # False

print(v and f) # False
print(v and v) # True
print(f and f) # False
print(v or f) # True
print(v or v) # True
print(f or f) # False
print(not v) # False
print(not f) # True

print(5>3) # True
print(5<3) # False
print(5>=3) # True
print(5<=3) # False
print(5==3) # False
print(5!=3) # True

print(type(v)) # <class 'bool'>
print(type(f)) # <class 'bool'>

print(bool("Hola mundo")) # True porque es string y tiene contenido
print(bool("")) # False porque es string vacío

print(bool(123)) # True porque es un número diferente de cero

print(bool(0)) # False porque es un número igual a cero
print(bool(None)) # False porque es None

print(bool([])) # False porque es una lista vacía
print(bool({})) # False porque es un diccionario vacío

print(bool(["Manzana", "Pera"])) # True porque es una lista con contenido

print(bool({"Nombre":"Juan"})) # True porque es un diccionario con contenido

x = 123
print(isinstance(x, int)) # True porque x es un entero

x = 123.45
print(isinstance(x, int)) # False porque x es un float
print(isinstance(x, float)) # True porque x es un float
