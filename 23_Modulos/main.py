# Separar el código en módulos hace que cada archivo tenga una funcionalidad distinta. 
# Así, el proyecto es más legible y mantenerlo resulta más sencillo. 
# Ya con funciones ahorras líneas; con módulos das un paso más: múltiples archivos bien organizados.

# - Cada archivo con responsabilidad clara.
# - Reutilización de funciones sin duplicar código.
# - Lectura más rápida y mantenimiento simple.

""" import operaciones  # Importa el módulo 'operaciones' que contiene funciones matemáticas


print(operaciones.sumar(2, 3))        # Llama a la función sumar del módulo operaciones
print(operaciones.restar(10, 4))      # Llama a la función  restar del módulo operaciones
print(operaciones.multiplicar(2, 6))  # Llama a la función multiplicar del módulo operaciones
print(operaciones.dividir(8, 2))      # Llama a la función dividir del módulo operaciones """

# Al usar módulos, puedes organizar tu código en archivos separados según su funcionalidad. 
# Esto facilita la lectura, el mantenimiento y la reutilización del código en diferentes proyectos.

# Para evitar poner operaciones varias veces, utiliza from ... import ...

from operaciones import sumar, restar, multiplicar, dividir

print(sumar(2, 3))          # Llama a la función sumar directamente
print(restar(10, 4))       # Llama a la función restar directamente
print(multiplicar(2, 6))   # Llama a la función multiplicar directamente
print(dividir(8, 2))      # Llama a la función dividir directamente

