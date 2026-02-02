"""
Para la opción 1, se crea **pedidos.py** con una función que imprime una lista de cafés 
y solicita una **opción**. 
Se define un **diccionario** para mapear números a nombres de cafés. 
Más adelante, esa elección se guardará en un archivo para alimentar el historial.

Puntos clave:
- **Función dedicada**: separar la lógica de pedidos.
- **Diccionario** para mapear opciones a cafés.
- **Entrada del usuario** con *input* y texto claro.
"""


def pedir_cafe():
    print("\nElige el café que prefieras:")
    print("1. Expreso")
    print("2. Capuchino")
    print("3. Latte")
    print("4. Americano")

    opcion = input("Opción: ")

    cafes = {
        "1": "Expreso",
        "2": "Capuchino",
        "3": "Latte",
        "4": "Americano"
    }
    # la elección y el guardado en archivo se implementarán más adelante