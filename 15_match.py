# Sentencia match

dia = 1

match dia: # Busca que coincida dia con la variable dia definida arriba. 
    case 1:
        print("Lunes") # Si dia es igual a 1, imprime lunes.
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("No es un dia valido")


dia = 3

match dia: # Busca que coincida dia con la variable dia definida arriba. 
    case 1:
        print("Lunes") 
    case 2:
        print("Martes")
    case 3:
        print("Miercoles") # Si dia es igual a 3, imprime Miercoles.
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("No es un dia valido")


dia = 8

match dia: # Busca que coincida dia con la variable dia definida arriba. 
    case 1:
        print("Lunes") 
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("No es un dia valido") # Si dia no coincide con los casos anteriores, imprime No es un dia valido.



"""
EJERCICIO: Match-Case con Equipos de Baloncesto Colombiano
============================================================
Aprende a usar match-case identificando equipos históricos de la 
Liga Colombiana de Baloncesto y sus ciudades.
"""

# Variable que representa un equipo de baloncesto colombiano

print("\n\nEJERCICIO: Match-Case con Equipos de Baloncesto Colombiano\n")

equipo = "Piratas de Bogotá"

print("=" * 60)
print("🏀 IDENTIFICADOR DE EQUIPOS DE BALONCESTO COLOMBIANO 🏀")
print("=" * 60)
print(f"\nEquipo ingresado: {equipo}\n")

# Estructura match-case para identificar equipos
match equipo:
    case "Piratas de Bogotá":
        print("🏴‍☠️ ¡Arr! Los Piratas de Bogotá navegan la cancha!")
        print("📍 Ciudad: Bogotá D.C.")
        print("🏆 Múltiples campeonatos en su historia")
        
    case "Titanes de Barranquilla":
        print("⚡ ¡Los Titanes dominan la costa caribeña!")
        print("📍 Ciudad: Barranquilla")
        print("🌊 El poder del Caribe en cada jugada")
        
    case "Búcaros de Bucaramanga":
        print("🦅 ¡Los Búcaros vuelan alto en Santander!")
        print("📍 Ciudad: Bucaramanga")
        print("⛰️ La garra de la montaña santandereana")
        
    case "Cimarrones del Chocó":
        print("🐆 ¡Los Cimarrones representan al Pacífico!")
        print("📍 Ciudad: Quibdó")
        print("🌴 La fuerza del Pacífico colombiano")
        
    case "Cafeteros de Armenia":
        print("☕ ¡Los Cafeteros con sabor del Eje Cafetero!")
        print("📍 Ciudad: Armenia, Quindío")
        print("🏔️ Baloncesto con aroma a café colombiano")
        
    case _:
        print("❌ Equipo no reconocido en la base de datos")
        print("💡 Equipos disponibles:")
        print("   • Piratas de Bogotá")
        print("   • Titanes de Barranquilla")
        print("   • Búcaros de Bucaramanga")
        print("   • Cimarrones del Chocó")
        print("   • Cafeteros de Armenia")

print("\n" + "=" * 60)

# ============================================================
# PRUEBAS CON DIFERENTES VALORES
# ============================================================

print("\n\n🧪 PROBANDO DIFERENTES EQUIPOS:\n")

# Lista de equipos para probar (incluye casos válidos e inválidos)
equipos_prueba = [
    "Titanes de Barranquilla",
    "Búcaros de Bucaramanga",
    "Aguacateros de Medellín",  # Este no existe (caso _)
    "Cimarrones del Chocó",
    "Cañeros de Cali"  # Este tampoco existe (caso _)
]

for i, equipo_test in enumerate(equipos_prueba, 1):
    print(f"\n--- Prueba {i} ---")
    print(f"Equipo: {equipo_test}")
    
    match equipo_test:
        case "Piratas de Bogotá":
            print("✅ Piratas - Bogotá D.C.")
        case "Titanes de Barranquilla":
            print("✅ Titanes - Barranquilla")
        case "Búcaros de Bucaramanga":
            print("✅ Búcaros - Bucaramanga")
        case "Cimarrones del Chocó":
            print("✅ Cimarrones - Quibdó")
        case "Cafeteros de Armenia":
            print("✅ Cafeteros - Armenia")
        case _:
            print("❌ Equipo no encontrado")

print("\n" + "=" * 60)

"""
📝 COMENTARIOS Y RESULTADOS PARA COMPARTIR:
=========================================================

🎯 OBJETIVO DEL EJERCICIO:
   Practicar la estructura match-case de Python 3.10+ usando datos
   del baloncesto colombiano como contexto educativo y cultural.

🔑 CONCEPTOS CLAVE:
   • match-case es similar al switch de otros lenguajes
   • Evalúa exactamente el valor (no usa operadores de comparación)
   • El caso _ funciona como "default" o "else"
   • Ideal para múltiples condiciones discretas

💡 APRENDIZAJES:
   1. Match-case hace el código más legible que múltiples if-elif
   2. El caso _ captura cualquier valor no especificado
   3. Es perfecto para menús, categorías o valores predefinidos
   4. Python 3.10+ requerido (versiones anteriores no lo soportan)

⚠️ DIFERENCIAS vs IF-ELIF:
   • Match-case: más limpio para valores exactos
   • If-elif: mejor para rangos y condiciones complejas

🏀 CONTEXTO CULTURAL:
   Este ejercicio usa equipos reales de la Liga Colombiana de 
   Baloncesto, conectando programación con cultura deportiva.

📊 RESULTADOS DE LAS PRUEBAS:
   ✅ Casos válidos: Funcionan correctamente
   ❌ Casos inválidos: Capturados por el caso _
   
🚀 EJERCICIOS ADICIONALES SUGERIDOS:
   • Agregar más información (estadísticas, jugadores destacados)
   • Crear un sistema de búsqueda por ciudad
   • Implementar un mini-juego de trivia de baloncesto
   • Agregar validación de entrada del usuario con input()

💪 DESAFÍO: 
   ¿Puedes modificar este código para incluir posiciones de 
   jugadores (Base, Escolta, Alero, Ala-Pívot, Pívot) y 
   mostrar características de cada posición?
"""
