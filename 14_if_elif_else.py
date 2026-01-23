# if - elif - esle

if 5 > 3:
    print("5 es mayor que 3!") # La instrucción se ejecuta solo si la condición es verdadera

if 2 > 3:
    print("2 es mayor que 3!") # La instrucción NO se ejecuta si la condición NO es verdadera

X=5
Y=3

if X > Y:
    print("5(x) es mayor que 3(y)!") # La instrucción se ejecuta solo si la condición es verdadera

if X < Y:
    print("5 es menor que 3!") # La instrucción NO se ejecuta si la condición NO es verdadera

if X > Y:
    print("X es mayor que Y!") # La instrucción se ejecuta solo si la condición es verdadera
elif X == Y:
    print("X es igual a Y!") # La instrucción se ejecuta solo si la condición es verdadera
else:
    print("X es menor que Y!") # La instrucción se ejecuta solo si la condición es verdadera

X=5
Y=5

if X > Y:
    print("X es mayor que Y!")
elif X == Y:
    print("X es igual a Y!")
else:
    print("X es menor que Y!")

X=5
Y=7

if X > Y:
    print("X es mayor que Y!")
elif X == Y:
    print("X es igual a Y!")
else:
    print("Ninguna de las condiciones anteriores se cumplió")


x=5
y=3
z=1

if x > y and x > z:
    print("X es el número más grande!") # AND = Ambas condiciones deben cumplirse


x=5
y=3
z=10

if x > y and x > z:
    print("X no es mayor que Y!")
elif X == Y :
    print("X es igual a Y!")
else:
    print("Ninguna de las condiciones anteriores se cumplió")


x=5
y=3
z=10

if x > y or x > z:
    print("X es mayor que Y ó X es menor a Z!") # Una de las dos condiciones se cumple
elif X == Y :
    print("X es igual a Y!")
else:
    print("Ninguna de las condiciones anteriores se cumplió")


a="Python"
b="Java"
c="Python"

if a == b:
    print("a es igual a b")
elif a == c:
    print("a es igual a c") # La instrucción se ejecuta solo si la condición es verdadera
else:
    print("Ninguna de las condiciones anteriores se cumplió")


a="Python"
b="Java"
c="Python"

if a == c:
    if a == b:
        print("a es igual a c, pero es distinto de b") # Es importante la indentación.
    else:
        print("Estoy saliento por el Else del IF interno") # La instrucción se ejecuta solo si la condición es verdadera. 
else:
    print("Ninguna de las condiciones anteriores se cumplió")



e = 10
f = 10

if e == f:
    # No sé que hacer si estas dos variables son iguales.
    # No se puede dejar vacío el bloque.
    # Se usa el statement pass para evitar errores de sintaxis.
    pass # La instrucción pass se utiliza para evitar errores de sintaxis.

else:
    print("Ninguna de las condiciones anteriores se cumplió")