# # Leer todo el contenido
# file = open("mi_archivo.txt", "r")
# contenido = file.read()
# print("el contenido completo:\n", contenido)
# file.close()

# # Leer una sola línea
# file = open("mi_archivo.txt", "r")
# linea = file.readline()
# print("la primera linea: ", linea)
# file.close()

# # Añadir contenido a un archivo existente
# file = open("mi_archivo.txt", "a")
# file.write("\nAñadiendo otra línea al final.")
# file.close()

# # Leer todo el contenido
# file = open("mi_archivo.txt", "r")
# contenido = file.read()
# print("el contenido completo con append:\n", contenido)
# file.close()

# # Escribir en un archivo
# file = open("mi_archivo.txt", "w")
# file.write("Esto es una nueva línea de texto.")
# file.close()

# # Leer todo el contenido
# file = open("mi_archivo.txt", "r")
# contenido = file.read()
# print("el contenido completo con write:\n", contenido)
# file.close()

# Usando 'with' para manejar archivos
with open("mi_archivo.txt", "r") as file:
    contenido = file.read()
    print(contenido)