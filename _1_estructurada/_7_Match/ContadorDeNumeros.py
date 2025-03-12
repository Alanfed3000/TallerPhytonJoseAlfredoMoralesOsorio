import sys

if __name__ == '__main__':
    lista = [1, 3, 6, 0, 9, 2, 7, 4, 8, 3, 2, 7, 3, 6, 4, 2, 9, 7, 6, 4, 2, 7, 3, 8, 5, 8, 2, 7, 4, 9, 4, 3, 7, 4, 8, 2,
             9, 9, 4, 7, 2, 0]
    totales = [0] * 10  # Para contar del 0 al 9
    adoptados = int=0

    for elemento in lista:
        match elemento:
            case 1:
                totales[1] += 1
            case 2:
                totales[2] += 1
            case 3:
                totales[3] += 1
            case 4:
                totales[4] += 1
            case 5:
                totales[5] += 1
            case 6:
                totales[6] += 1
            case 7:
                totales[7] += 1
            case 8:
                totales[8] += 1
            case 9:
                totales[9] += 1
            case _:
                adoptados += 1

    print("Conteo de números:")
    for i in range(1, 10):
        print(f"Número {i}: .-{totales[i]} veces")


