if __name__ == '__main__':
    # Usar una tupla como clave en un diccionario
    diccionario = {}

    # Agregar tupla como clave
    diccionario[("Ana", 25)] = "Estudiante"
    diccionario[("Luis", 30)] = "Ingeniero"
    diccionario[("Carlos", 40)] = "Abogado"

    # Acceder a los valores del diccionario usando la tupla
    ocupacion_ana = diccionario[("Ana", 25)]
    ocupacion_luis = diccionario[("Luis", 30)]
    ocupacion_carlos = diccionario[("Carlos", 40)]

    print(f"Ana es: {ocupacion_ana}")
    print(f"Luis es: {ocupacion_luis}")
    print(f"Carlos es: {ocupacion_carlos}")