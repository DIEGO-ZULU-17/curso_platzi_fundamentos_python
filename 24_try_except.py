# Python ofrece una estructura simple para el manejo de errores. 
# El bloque try intenta ejecutar código y el bloque except captura la excepción si ocurre un problema. 
# Usarlo de forma consciente mejora la legibilidad y la estabilidad del programa.

# Ejemplo básico de uso de try y except
try:
    print("\n")
    print("Intentamos algo")
except:
    print("Captura error")

################################################################################

# Ejemplo con manejo específico de excepción

# Sin manejo:
print("\n")

#resultado = 10 / 0  # Provoca ZeroDivisionError`
#print(resultado)

print("\n")

# Con manejo específico:
try:
    resultado2 = 10 / 0
    print(resultado2)
except ZeroDivisionError: # Es buena práctica capturar excepciones específicas y poner el nombre de la excepción.
    print("No se puede dividir por cero.")

################################################################################

# Ejemplo con una variable no definida
print("\n")

# Sin manejo:
#print(x)  # Provoca NameError`

# Con manejo específico:
try:
    print(x)
except NameError: # Captura la excepción NameError
    print("Esta variable no ha sido definida.")

################################################################################

# Uso de finally
print("\n")

# Con error presente:
try:
    print(y)  # y no definida
except NameError:
    print("\n")
    print("Esta variable no ha sido definida.")
finally:
    print("\n")
    print("Esto se ejecuta siempre.")

# Sin error:
y = 1
try:
    print(y)  # y está definida
except NameError:
    print("\n")
    print("Esta variable no ha sido definida.")
finally:
    print("\n")
    print("Esto se ejecuta siempre.")

################################################################################

# Uso de else
print("\n")

# Con error presente:
try:
    resultado3 = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")
else:
    print("La división se realizó correctamente:", resultado3)

# Sin error:
try:
    resultado4 = 10 / 2
except ZeroDivisionError:
    print("No se puede dividir por cero.")
else:
    print("\n")
    print("La división se realizó correctamente:", resultado4)


################################################################################

# Múltiples excepciones
print("\n")
try:
    valor = int(input("Ingresa un número entero: "))
    resultado5 = 10 / valor
except ValueError:
    print("Error: Debes ingresar un número entero válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print("El resultado de la división es:", resultado5)

################################################################################

# Captura de todas las excepciones
print("\n")
try:
    valor = int(input("Ingresa un número entero nuevo: "))
    resultado6 = 10 / valor
except Exception as e:  # Captura cualquier excepción y la almacena en 'e'
    print("Ocurrió un error:", e)
else:
    print("El resultado de la división es:", resultado6)

################################################################################

# Lanzar excepciones manualmente
print("\n")

def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    elif edad < 18:
        raise ValueError("Debes ser mayor de edad.")
    else:
        return "Edad válida."
try:
    edad_usuario = int(input("Ingresa tu edad: "))
    mensaje = verificar_edad(edad_usuario)
    print(mensaje)
except ValueError as e: # La e almacena el mensaje de la excepción lanzada.
    print("Error:", e)

################################################################################