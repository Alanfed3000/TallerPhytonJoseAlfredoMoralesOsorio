# return suma
# def potencia(x: int) -> int:
# return int(pow(x, 2))


if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19]

    print(f"Numeros originales: {numeros}")

    print(f"La suma total con una funcion: {(numeros)}")

    numerosCuadrados = list(map(lambda x: x * x, numeros))
    print(f"Numeros Cuadrados con una funcion: {numerosCuadrados}")
