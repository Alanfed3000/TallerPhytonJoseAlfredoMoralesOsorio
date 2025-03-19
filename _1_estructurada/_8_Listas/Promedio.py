import statistics as cuyo

if __name__ == '__main__':
    numeros = [10, 20, 50, 80, 90, 30, 40]
    # Opcion lenta
    conteo=0
    suma=0
    promedio=0
    for valor in numeros:
        suma+=valor
        conteo+=1

    promedio=suma/conteo
    print(promedio)

    # Opcion Medio lenta
    suma=0
    for valor in numeros:
        suma+=valor
    promedio=suma/len(numeros)
    print(promedio)

    # Opcion rapida
    promedio== cuyo.mean(numeros)
    print(promedio)
