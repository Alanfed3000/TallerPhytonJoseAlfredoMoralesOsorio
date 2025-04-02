import json
import sys


def iterador():

    archivo = open("Datos.json","r", encoding= "utf-8")
    try:
        datos= json.load(archivo)
        for persona in datos["usuarios"]:
            yield (persona["Id"], persona["Nombre"], persona["Edad"], persona["RFC"])

    except FileNotFoundError:
        print(RED,"!Error! El archivo no existe.")
    except json.JSONDecodeError:
        print(RED,"!Error! El archivo no contiene un JSON válido.")
    except Exception as e:
        print(GREEN,"Pues no se que ocurrio:", e)

    finally:
        archivo.close()
        print(RESET,"archivo Json cerrado")



if __name__ == '_main_':

    # Definición de códigos ANSI
    RESET = "\033[0m"  # Restablece el color a su valor por defecto
    # Colores de texto
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    # Colores de fondo
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    i = 1

    for Id, nombre, edad, RFC in iterador():

        match i:
            case 1:
                sys.stdout.write(RED)
            case 2:
                sys.stdout.write(GREEN)
            case 3:
                sys.stdout.write(BLUE)
            case _:
                sys.stdout.write(RESET)

        print("Id: ", id)
        print("Nombre: ", nombre)
        print("Edad: ", edad)
        print("RFC: ", RFC)
        print("-----------------------------")


        i+=1