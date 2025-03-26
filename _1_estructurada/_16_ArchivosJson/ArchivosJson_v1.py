import json

if __name__ == '__main__':
# Version corta de abrir un archivoo Jason
# Abre el archivo Json en modo de lectura y with se encarga de
with open("datos.jason", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo) # Carga el contenido del archivo JSON

# Muestra el contenido del JSON
for persona in datos["personas"]:
    print("Nombre:", persona["nombre"])
    print("Edad:", persona["edad"])
    print("Ciudad:", persona["ciudad"])
    print("Estado:", persona["estado"])
    print("----------------------------------:") # Linea en blanco para