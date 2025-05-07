if __name__ == '__main__':
    palabra: str = "%s"
    lista: list = ["nombre", "apellido_paterno", "nombre_usuario", "correo_electronico", "contrasennia"]

    print(palabra)
    # palabra=palabra * 5
    print(palabra)

    t = len(lista)  # Obtiene el total de elementos de una lista
    print(t)

    palabra = palabra * len(lista)
    print(palabra)

    campos = ", ".join(lista)  # //"nombre", "apellido_paterno", "nombre_usuario", "correo_electronico", "contrasennia"
    print(campos)

    querySQL = f"INSERT INTO {campos} ( {campos} )"
    print(querySQL)

