# Diccionario en Python
# Los diccionarios en Python son una colección poderosa y ordenada desde Python 3.7 
# que organiza datos en pares clave-valor.

# Crear un diccionario
auto = {
    'marca': 'Renault',
    'modelo': 'Clio',
    'año': 2025
}

print("\n")
print(auto)
print("\n")

# Imprimir información parcial

print(auto['marca'])      # Renault
print("\n")
print(auto.get('marca'))  # Renault
print("\n")

# Key = Clave
# Value = Valor

# Solo imprimir las claves
# Se imprimen de forma ordenada desde Python 3.7.
print(auto.keys())  # dict_keys(['marca', 'modelo', 'año'])
print("\n")

# Solo imprimir los valores
print(auto.values())  # dict_values(['Renault', 'Clio', 2025
print("\n")

# Comprueba si una clave existe con in. Recuerda: es case sensitive.

if 'marca' in auto:
    print('Marca es una de las propiedades de este diccionario')

print("\n")

if 'MARCA' in auto:  # no entra por sensibilidad a mayúsculas
    print('No se imprime')


# Modificar el valor de una clave existente
auto['año'] = 2020
print(auto)  # {'marca': 'Renault', 'modelo': 'Clio', 'año': 2020}
print("\n")

# Agregar una nueva clave-valor
auto['color'] = 'Verde'
print(auto)  # {'marca': 'Renault', 'modelo': 'Clio', 'año': 2020, 'color': 'Verde'}
print("\n")

# Uso de Update para modificar o agregar pares clave-valor
# Se puede hacer en diferentes líneas o en una sola línea.
auto.update({'año': 2022})
auto.update({'año': '2022', 'puertas': '4'})
print(auto)  # {'marca': 'Renault', 'modelo': 'Clio', 'año': '2022', 'color': 'Verde', 'puertas': '4'}
print("\n")

# Eliminar un par clave-valor
# Usando pop()
auto.pop('puertas')
print(auto)  # {'marca': 'Renault', 'modelo': 'Clio', 'año': '2022', 'color': 'Verde'}
print("\n")

# Usando popitem() elimina el último par clave-valor agregado
auto.popitem()
print(auto)  # {'marca': 'Renault', 'modelo': 'Clio', 'año': '2022'}
print("\n")

# Metodo clear() para vaciar el diccionario
auto.clear()
print(auto)  # {}
print("\n")

# Crear un diccionario
auto = {
    'marca': 'Renault',
    'modelo': 'Clio',
    'año': 2025
}

print("\n")
print(auto)
print("\n")

# Recorrer un diccionario

# Solo claves
for k in auto: # La k es de keys (clave)
    print(k)
print("\n")

# Solo valores
for v in auto.values():
    print(v) # La v es de values (valores)
print("\n")

# Clave y valor al mismo tiempo
for k, v in auto.items():
    print(k, v)
print("\n")


# Diccionarios anidados

familia = {
    'hijo uno':  {
        'nombre': 'Pedro',   
        'edad': 8
        },
    'hijo dos':  {
        'nombre': 'Ana',     
        'edad': 7
        },
    'hijo tres': {
        'nombre': 'Marcelo', 
        'edad': 6
        }
}

print(familia['hijo uno']['nombre'])  # Pedro
print("\n")

print(familia['hijo dos']['edad'])    # 7
print("\n")

# Recorrer un diccionario anidado
for hijo, info in familia.items():
    print(hijo)
    for k, v in info.items():
        print(f"  {k}: {v}")
    print("\n")

# En otros lenguajes los diccionarios se conocen como "objetos directos" o "hashes".


