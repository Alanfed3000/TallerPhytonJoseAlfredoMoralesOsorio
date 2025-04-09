# Desarrolla un programa en python en que utilice
# la POO para registrar un libro (ISBN, TITULO
# y Autor)
# Los atributos debe estar en privado
# debes tener un constructor para el registro
# Debes tener solo getters de cada atributo

# En otra clase debera registrar una coleccion
# de libros
# En esta clase debes tener add, delete y show
class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str):
        self.__isbn = isbn
        self.__titulo = titulo
        self.__autor = autor

    def get_isbn(self) -> str:
        return self.__isbn

    def get_titulo(self) -> str:
        return self.__titulo

    def get_autor(self) -> str:
        return self.__autor


class ColeccionLibros:
    def __init__(self):
        self.__libros = []

    def add_libro(self, libro: Libro):
        self.__libros.append(libro)

    def delete_libro(self, isbn: str):
        self.__libros = [libro for libro in self.__libros if libro.get_isbn() != isbn]

    def show_libros(self):
        for libro in self.__libros:
            print(f"ISBN: {libro.get_isbn()}")
            print(f"Título: {libro.get_titulo()}")
            print(f"Autor: {libro.get_autor()}")
            print("----------------------------")


if __name__ == "__main__":
    coleccion = ColeccionLibros()

    libro1 = Libro("6079000326", "Santiago y el Talisman de la Luz", "Rosana Curiel Defossé")
    libro2 = Libro("9786077476719", "Abitos Atomicos", "James Clear")
    libro3 = Libro("978-0140275360", "Pscologia", "Jane Austen")

    coleccion.add_libro(libro1)
    coleccion.add_libro(libro2)
    coleccion.add_libro(libro3)

    print("Lista de libros:")
    coleccion.show_libros()

    coleccion.delete_libro("6079000326")

    print(f"Lista de libros después de eliminar un libro:")
    coleccion.show_libros()
