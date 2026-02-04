"""
El menú se encapsula en un módulo separado para mantener el flujo principal
limpio y modular. Ahora incluye múltiples funciones para mostrar diferentes
categorías de bebidas con formato mejorado.

Puntos clave:
- **Modularidad**: funciones dedicadas para cada menú.
- **Formato visual**: separadores y estructura clara.
- **Extensibilidad**: fácil agregar nuevas categorías.
"""

def mostrar_menu():
    print("\n" + "="*40)
    print("     BIENVENIDO A LA MÁQUINA DE BEBIDAS")
    print("="*40)
    print("1. Pedir una bebida")
    print("2. Ver el historial de pedidos")
    print("3. Salir")
    print("="*40)

def mostrar_categorias():
    print("\n¿Qué tipo de bebida deseas?")
    print("1. Cafés")
    print("2. Tés")
    print("3. Jugos Naturales")
    print("4. Refrescos")
    print("5. Volver al menú principal")
