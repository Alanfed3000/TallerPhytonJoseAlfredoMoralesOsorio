import json

if __name__ == '__main__':
    try:
        with open("data.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        for persona in datos:
            print("Nombre:", persona["Nombre"])
            print("Edad:", persona["Edad"])
            try:
                print("RFC:", persona["RFC"])
            except KeyError:
                print("RFC: No especificado")
            print("ID:", persona["id"])
            if persona["Edad"]>=18:
              print(f'{persona["Nombre"]} es mayor de edad')
            else:
              print(f'{persona["Nombre"]} es menor de edad')
            print("----------------------------------:")
    except FileNotFoundError:
        print("Error: El archivo 'data.json' no fue encontrado.")
    except json.JSONDecodeError:
        print("Error: El archivo 'data.json' no tiene un formato JSON válido.")