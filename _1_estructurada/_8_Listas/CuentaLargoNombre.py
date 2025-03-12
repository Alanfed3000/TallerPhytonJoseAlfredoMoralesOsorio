if __name__ == '__main__':
    n = int(input("¿Cuántos nombres quieres?: "))
    indios = [0] * 10  # Contadores para nombres de 1 a 10 letras
    extras = 0  # Nombres con más de 10 letras

    for _ in range(n):
        nombre = str(input("Proporciona el Nombre: "))
        tam = len(nombre)

        match tam:
            case 1:
                indios[0] += 1
            case 2:
                indios[1] += 1
            case 3:
                indios[2] += 1
            case 4:
                indios[3] += 1
            case 5:
                indios[4] += 1
            case 6:
                indios[5] += 1
            case 7:
                indios[6] += 1
            case 8:
                indios[7] += 1
            case 9:
                indios[8] += 1
            case 10:
                indios[9] += 1
            case _:
                extras += 1

    for i, elemento in enumerate(indios, start=1):
        print(f"El total de nombres con {i} letra(s): {elemento}")

    print(f"El total de nombres con más de 10 letras: {extras}")
