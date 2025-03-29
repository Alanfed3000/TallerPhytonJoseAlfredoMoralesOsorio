def agregar_libro(biblioteca, titulo, autor, genero, copias):
    biblioteca[titulo] = {
        "autor": autor,
        "genero": genero,
        "copias_disponibles": copias,
        "copias_totales": copias,
    }
    print(f"Libro '{titulo}' agregado.")

def buscar_libros(biblioteca, **kwargs):
    resultados = []
    for titulo, detalles in biblioteca.items():
        if "titulo" in kwargs and kwargs["titulo"].lower() in titulo.lower():
            resultados.append((titulo, detalles))
        elif "autor" in kwargs and kwargs["autor"].lower() in detalles["autor"].lower():
            resultados.append((titulo, detalles))
        elif "genero" in kwargs and kwargs["genero"].lower() in detalles["genero"].lower():
            resultados.append((titulo, detalles))
    return resultados

def prestar_libro(biblioteca, titulo):
    if titulo in biblioteca and biblioteca[titulo]["copias_disponibles"] > 0:
        biblioteca[titulo]["copias_disponibles"] -= 1
        print(f"Libro '{titulo}' prestado.")
    else:
        print(f"No hay copias disponibles de '{titulo}'.")

def devolver_libro(biblioteca, titulo):
    if titulo in biblioteca and biblioteca[titulo]["copias_disponibles"] < biblioteca[titulo]["copias_totales"]:
        biblioteca[titulo]["copias_disponibles"] += 1
        print(f"Libro '{titulo}' devuelto.")
    else:
        print(f"El libro '{titulo}' no está prestado o no existe.")

def mostrar_libros_disponibles(biblioteca):
    for titulo, detalles in biblioteca.items():
        print(f"- {titulo} (Autor: {detalles['autor']}, Género: {detalles['genero']}, Copias disponibles: {detalles['copias_disponibles']})")
        yield titulo, detalles

def main():
    biblioteca = {}
    while True:
        print("\n=== Sistema de Gestión de Biblioteca ===")
        print("1. Agregar libro")
        print("2. Buscar libros")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Mostrar libros disponibles")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            copias = int(input("Número de copias: "))
            agregar_libro(biblioteca, titulo, autor, genero, copias)
        elif opcion == "2":
            print("Buscar por:")
            print("1. Título")
            print("2. Autor")
            print("3. Género")
            opcion_busqueda = input("Elige una opción de búsqueda: ")
            if opcion_busqueda == "1":
                titulo = input("Título a buscar: ")
                resultados = buscar_libros(biblioteca, titulo=titulo)
            elif opcion_busqueda == "2":
                autor = input("Autor a buscar: ")
                resultados = buscar_libros(biblioteca, autor=autor)
            elif opcion_busqueda == "3":
                genero = input("Género a buscar: ")
                resultados = buscar_libros(biblioteca, genero=genero)
            else:
                print("Opción de búsqueda inválida.")
                continue

            if resultados:
                print("\nResultados de la búsqueda:")
                for titulo, detalles in resultados:
                    print(f"- {titulo} (Autor: {detalles['autor']}, Género: {detalles['genero']}, Copias disponibles: {detalles['copias_disponibles']})")
            else:
                print("No se encontraron libros.")
        elif opcion == "3":
            titulo = input("Título del libro a prestar: ")
            prestar_libro(biblioteca, titulo)
        elif opcion == "4":
            titulo = input("Título del libro a devolver: ")
            devolver_libro(biblioteca, titulo)
        elif opcion == "5":
            print("\nLibros disponibles:")
            list(mostrar_libros_disponibles(biblioteca)) # consume el iterador
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()