"""
Lectura mejorada del historial con soporte para formato con timestamps.
Utiliza try/except para manejar archivos inexistentes.
Muestra el historial con formato estructurado y numerado.
"""

ARCHIVO_PEDIDOS = "pedidos2.txt" # Se copia desde pedidos.py para mantener la coherencia.

def ver_historial():
    """Muestra el historial de pedidos con formato mejorado."""
    try:
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            
            if pedidos:
                print("\n" + "="*60)
                print(" "*15 + "HISTORIAL DE PEDIDOS")
                print("="*60)
                
                for indice, pedido in enumerate(pedidos, start=1):
                    pedido_limpio = pedido.strip()
                    # Mostrar con formato mejorado
                    print(f"{indice:2d}. {pedido_limpio}")
                
                print("="*60)
                print(f"Total de pedidos: {len(pedidos)}")
                print("="*60 + "\n")
            else:
                print("\nAún no hay ningún pedido registrado.\n")
    except FileNotFoundError:
        print("\nNo hay historial de pedidos aún. ¡Haz tu primer pedido!\n")

def ver_historial_filtrado(categoria=None):
    """Muestra el historial filtrado por categoría (opcional)."""
    try:
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            
            if categoria:
                pedidos_filtrados = [p for p in pedidos if categoria.lower() in p.lower()]
            else:
                pedidos_filtrados = pedidos
            
            if pedidos_filtrados:
                print(f"\n" + "="*60)
                titulo = f"HISTORIAL DE {categoria.upper()}" if categoria else "HISTORIAL DE PEDIDOS"
                print(f" "*(60 - len(titulo))//2 + titulo)
                print("="*60)
                
                for indice, pedido in enumerate(pedidos_filtrados, start=1):
                    print(f"{indice:2d}. {pedido.strip()}")
                
                print("="*60 + "\n")
            else:
                print(f"\nNo hay pedidos de {categoria} registrados.\n")
    except FileNotFoundError:
        print("\nNo hay historial de pedidos aún.\n")