"""
La lectura del historial requiere contemplar que el archivo no exista aún. 
Se utiliza try/except para capturar FileNotFoundError. 
Si hay contenido, se muestra numerado con enumerate(start=1) 
y cada línea se limpia con strip para quitar el salto de línea.
"""

ARCHIVO_PEDIDOS = "pedidos.txt" # Se copia desde pedidos.py para mantener la coherencia.

def ver_historial():
    try:
        print("\n Historial de pedidos:")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo: # Leer el archivo en modo lectura.
            pedidos = archivo.readlines() # Leer todas las líneas y guardarlas en una lista.
            if pedidos:
                for indice, pedido in enumerate(pedidos, start=1): # enumerate para numerar desde 1, lo que hace enumerate es devolver tuplas (índice, valor)  
                    print(str(indice) + ". " + pedido.strip()) # strip para eliminar saltos de línea u otros espacios.
                    # str(indice) convierte el índice a cadena para concatenar.
            else: # Si el archivo está vacío.
                print("Aún no hay ningún pedido.")
    except FileNotFoundError:
        print("No hay historial de pedidos aún.")
            