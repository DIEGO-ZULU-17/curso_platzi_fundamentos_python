# **Máquina de café en Python con menú interactivo por terminal**

""" Construye una máquina de café en Python que funciona en la terminal 
con un flujo claro, organizado en módulos y controlado por un bucle 
infinito con salidas seguras. Aquí verás cómo usar *while True*, 
*input*, *if/elif/else*, *break* y *pass* para orquestar opciones 
como pedir un café, ver el historial y salir. 
Todo con un punto de entrada fiable usando *if **name** == "**main**"*. """

"""
## ¿Cómo se define el flujo principal en main.py?

El corazón del programa vive en una función **main** dentro de **main.py**. 
Se utiliza un **bucle while** con condición verdadera para mantener 
la interacción activa, y se interrumpe con **break** cuando la persona elige salir. 
La entrada del usuario se captura con *input*, que devuelve siempre una cadena, 
así que se comparan valores como "1", "2" y "3". Para partes aún no implementadas, 
se usa **pass**.

Puntos clave:
- **Bucle infinito controlado** con *while True* y cortes con *break*.
- **Entrada por terminal** con *input* y opciones en texto.
- **Ramas condicionales** con *if/elif/else* para navegar el menú.
- **Marcador de entrada del programa** con *if **name** == "**main**"*.

"""

from menu import mostrar_menu
from pedidos import pedir_cafe
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while True: # Bucle infinito para el menú. Se rompera con break cuando necesitemos. 
        # Mostrar el menú principal
        mostrar_menu()

        # Pedir opción al usuario
        opcion = input("Selecciona una opción: ") # Input siempre devuelve una cadena str.

        if opcion == "1":
            # Pedir un café (lógica ampliada más adelante)
            pedir_cafe()
            # pass # Placeholder para futura implementación
        elif opcion == "2":
            # Ver historial (se implementará leyendo un archivo)
            ver_historial()
            # pass
        elif opcion == "3":
            print("\nMuchas gracias por haber tomado nuestros riquísimos cafés.")
            break # Salir del bucle y terminar el programa.
        else:
            print("Opción inválida. Por favor, indique una de las opciones sugeridas.")

if __name__ == "__main__": # Nos aseguramos que main se ejecute solo si este archivo es el principal.
    main() # Si se ejecuta de otra forma, no funcionará porque debe cumplir la condición anterior.

"""
if __name__ == "__main__": asegura que cierto código solo se ejecute cuando el archivo 
es el programa principal y no cuando es importado como un módulo. 
Es crucial para organizar tu proyecto en múltiples archivos, 
permitiendo que cada módulo tenga su propia lógica sin ejecutarla 
automáticamente al importarlo en otro lugar. Facilita la modularización y 
evita ejecuciones no deseadas.
"""