"""
Módulo de pedidos mejorado que soporta múltiples categorías de bebidas.
Guarda los pedidos con timestamp para un historial más detallado.

Puntos clave:
- **Múltiples categorías** de bebidas.
- **Timestamp** para cada pedido.
- **Diccionarios anidados** para organizar las opciones.
- **Formato estructurado** del historial.
"""

from datetime import datetime

ARCHIVO_PEDIDOS = "pedidos2.txt" # Las constantes van en mayúsculas por convención.

# Diccionarios de bebidas por categoría
cafes = {
    "1": "Expreso",
    "2": "Capuchino",
    "3": "Latte",
    "4": "Americano",
    "5": "Café con leche"
}

tes = {
    "1": "Té Verde",
    "2": "Té Negro",
    "3": "Té de Manzanilla",
    "4": "Té de Jengibre"
}

jugos = {
    "1": "Jugo de Naranja",
    "2": "Jugo de Manzana",
    "3": "Jugo de Fresa",
    "4": "Jugo de Zanahoria"
}

refrescos = {
    "1": "Agua con Gas",
    "2": "Limonada",
    "3": "Agua Fresca",
    "4": "Smoothie de Frutas"
}

def guardar_pedido(bebida, categoria):
    """Guarda un pedido con timestamp en el archivo."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
        archivo.write(f"[{timestamp}] {categoria} - {bebida}\n")

def pedir_cafe():
    """Flujo principal de pedidos con categorías."""
    while True:
        print("\n¿Qué tipo de bebida deseas?")
        print("1. Cafés")
        print("2. Tés")
        print("3. Jugos Naturales")
        print("4. Refrescos")
        print("5. Volver al menú principal")
        
        categoria_opcion = input("Opción: ")
        
        if categoria_opcion == "1":
            procesar_categoria(cafes, "Café")
        elif categoria_opcion == "2":
            procesar_categoria(tes, "Té")
        elif categoria_opcion == "3":
            procesar_categoria(jugos, "Jugo Natural")
        elif categoria_opcion == "4":
            procesar_categoria(refrescos, "Refresco")
        elif categoria_opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

def procesar_categoria(bebidas_dict, nombre_categoria):
    """Procesa la selección de una categoría específica."""
    print(f"\nSelecciona tu {nombre_categoria.lower()} preferido:")
    for key, value in bebidas_dict.items():
        print(f"{key}. {value}")
    print(f"{len(bebidas_dict) + 1}. Atrás")
    
    opcion = input("Opción: ")
    
    if opcion in bebidas_dict:
        bebida_elegida = bebidas_dict[opcion]
        print(f"\n✓ Has pedido un {nombre_categoria.lower()}: {bebida_elegida}")
        print(f"¡Preparando tu {bebida_elegida}!\n")
        guardar_pedido(bebida_elegida, nombre_categoria)
    elif opcion == str(len(bebidas_dict) + 1):
        return
    else:
        print("Opción inválida. Por favor, elige de la lista.")