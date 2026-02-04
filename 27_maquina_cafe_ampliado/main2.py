from menu2 import mostrar_menu
from pedidos2 import pedir_cafe
from historial2 import ver_historial

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
            print("\nMuchas gracias por haber tomado nuestras riquísimas bebidas.")
            break # Salir del bucle y terminar el programa.
        else:
            print("Opción inválida. Por favor, indique una de las opciones sugeridas.")

if __name__ == "__main__": # Nos aseguramos que main se ejecute solo si este archivo es el principal.
    main() # Si se ejecuta de otra forma, no funcionará porque debe cumplir la condición anterior.
