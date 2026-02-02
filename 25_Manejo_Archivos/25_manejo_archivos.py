# Lectura y escritura de archivos de texto en Python

# open(nombre_archivo, modo)

# R = read (leer)
# RB = read binary (leer en binario)
# W = write (escribir, crea el archivo si no existe o lo sobreescribe si existe)
# WB = write binary (escribir en binario, crea el archivo si no existe o lo sobreescribe si existe)
# A = append (agregar al final del archivo, crea el archivo si no existe)
# AB = append binary (agregar al final del archivo en binario, crea el archivo si no existe)
# X = create (crear, crea el archivo solo si no existe, si existe lanza un error)
# XB = create binary (crear en binario, crea el archivo solo si no existe, si existe lanza un error)
# Modo por defecto es 'r' (leer)

#################################################################

# Ejemplo de lectura de un archivo de texto

""" f = open("archivo.txt", "r")  # Abrir el archivo en modo lectura. f es de file (archivo).

print(f.readline())  # Leer una línea del archivo.

f.close()  # Cerrar el archivo después de usarlo. """

# Es importante cerrar el archivo para liberar recursos del sistema.
# Nos dará un error "FileNotFoundError" porque el archivo no existe aún.

#################################################################

# Lo abrimos con un try-except para manejar el error
""" try:
    f = open("archivo.txt", "r")
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("El archivo no existe.") """

#########################################################################

# Ejemplo de with para manejar archivos

# Crea el archivo.txt antes de ejecutar este código.
# Debes ubicarte en la terminal en la carpeta donde está este archivo.txt.
# Utiliza "cd .\Ruta\De\La\Carpeta" para cambiar de carpeta: cd .\25_Manejo_Archivos\   

try:
    with open("archivo.txt", "r") as f: # La variable va al final. 
        print(f.readline()) # readline() lee una línea del archivo.
except FileNotFoundError:
    print("No se ha encontrado el archivo")

# Con with no es necesario cerrar el archivo, se cierra automáticamente al salir del bloque with.

try:
    with open("archivo.txt", "r") as f: # La variable va al final. 
        print(f.read()) # read() lee todo el contenido del archivo.
except FileNotFoundError:
    print("No se ha encontrado el archivo")
# Se imprime lÃnea porque está en formato unicode.
# Debemos pasarlo a formato UTF-8 para que lea los acentos y las ñ.

print("\n")
print("Leyendo con UTF-8:")

with open("archivo.txt", "r", encoding="utf-8") as f:
    print(f.read()) # Se leen las tildes y la ñ correctamente.

#######################################################################

# Ejemplo de sobre escritura en un archivo de texto = w

print("\n")
# Escribir (sobrescribe)
with open("archivo.txt", "w", encoding="utf-8") as f:
    f.write("hola mundo desde write en el with\n")

# Leer lo escrito
with open("archivo.txt", "r", encoding="utf-8") as f:
    print(f.readline()) # Se reemplazó la línea anterior.


#######################################################################

# Ejemplo de agregar texto al final de un archivo de texto = a

print("\n")
# Agregar (no sobrescribe)
with open("archivo.txt", "a", encoding="utf-8") as f:
    f.write("hola mundo desde append en el with\n")

# Leer lo escrito
with open("archivo.txt", "r", encoding="utf-8") as f:
    print(f.read()) # Se agregó la línea al final del archivo. 

# Agregar con salto de línea al final
print("\n")
with open("archivo.txt", "a", encoding="utf-8") as f:
    f.write("\n")  # Salto de línea
    f.write("hola mundo desde append en el with con salto de línea\n")

# Leer lo escrito
with open("archivo.txt", "r", encoding="utf-8") as f:
    print(f.read()) # Se agregó la línea al final del archivo. 

#######################################################################

# Ejemplo de crear un archivo de texto = x

print("\n")

try:
    with open("archivo2.txt", "r", encoding="utf-8") as f:
        print(f.readline())
except FileNotFoundError:
    print("No se ha encontrado el archivo")
    # Crear el archivo vacío si no existe usando x = create
    open("archivo2.txt", "x").close()
    # Escribir y leer a continuación
    with open("archivo2.txt", "w", encoding="utf-8") as f: # w = write
        f.write("hola mundo desde write en el with\n")
    with open("archivo2.txt", "r", encoding="utf-8") as f: # r = read
        print(f.readline())
    
#######################################################################

# Leer archivo en otra ruta: archivo3.txt

print("\n")

try:
    with open(r"C:\Users\diego\OneDrive\Desktop\PLATZI\Platzi_Fundamentos_Python\Fundamentos_Python\archivo3.txt", "r", encoding="utf-8") as f:
        print(f.read())  # Leer todo el contenido del archivo.
except FileNotFoundError:
    print("No se ha encontrado el archivo3.txt")     
# Utilizamos r antes de la ruta para indicar que es una cadena raw (cruda) 
# y evitar problemas con las barras invertidas.

