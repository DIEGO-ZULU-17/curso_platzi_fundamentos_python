"""
El menú se encapsula en un módulo separado para mantener el **flujo principal**
limpio y modular. Se imprime un encabezado con un salto de línea usando
"\n" y tres opciones: pedir un café, ver el historial y salir. Luego, 
se importa con *from menu import mostrar_menu*.

Puntos clave:
- **Modularidad**: un archivo dedicado para el menú.
- **Salida formateada** con *print* y saltos de línea.
- **Import explícito** de funciones para invocarlas desde el archivo principal.
"""

def mostrar_menu():
    print("\nBienvenido a la máquina de café")
    print("1. Pedir un café")
    print("2. Ver el historial de pedidos")
    print("3. Salir")
