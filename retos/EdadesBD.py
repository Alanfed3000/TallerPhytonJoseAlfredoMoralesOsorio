import json
import sys

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

def Mi_iterador():
    with open("Datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    for persona in datos["Usuarios"]:
        yield (persona["Id"], persona["Nombre"], persona["Edad"], persona["RFC"])

if __name__ == '__main__':

    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        # Recorre la lista de personas e imprime cada una
        i = 1

        for persona in datos["Usuarios"]: # Se usa Usuarios en vez de personas
            match i:
                case 1:
                    sys.stdout.write(RED)
                case 2:
                    sys.stdout.write(GREEN)
                case 3:
                    sys.stdout.write(BLUE)
                case _:
                    sys.stdout.write(RESET)

            print("Nombre:", persona["Nombre"])
            print("Edad:", persona["Edad"])
            print("RFC:", persona["RFC"])
            print("Id:", persona["Id"])
            print("-----------------------------")
            i += 1
    except FileNotFoundError:
        print("El archivo Datos.json no fue encontrado")
    except json.JSONDecodeError:
        print("El archivo Datos.json tiene un formato incorrecto")
    except KeyError:
        print("El archivo Datos.json no tiene la estructura correcta")

    for id, nombre, edad, RFC in Mi_iterador():
        print("Usuario:")
        print("Id: ", id)
        print("Nombre: ", nombre)
        print("Edad: ", edad)
        print("RFC: ", RFC)

        if edad >= 18:
            print(f"El usuario {id} es mayor de edad")
        else:
            print(f"El usuario {id} es menor de edad")

        print("-----------------------------")