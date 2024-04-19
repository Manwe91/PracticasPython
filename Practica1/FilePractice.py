# Abre un archivo llamado "archivo.txt" en modo lectura
with open("archivo.txt", "r") as archivo:
    # Realiza operaciones en el archivo
    # Por ejemplo, leer su contenido
    contenido = archivo.read()
    print(contenido)

with open("archivo.txt", "w") as archivo:
    archivo.write("/n Adios Mundo")
    archivo.close()

with open("archivo.txt", "r") as archivo:
    contenidoMod = archivo.read()
    print(contenidoMod)
    archivo.close()