if __name__ == '__main__':
    #añade un elemento a final de la lista
    mi_lista = [1, 2, 3]
    mi_lista.append(4)
    print(mi_lista)

    #Añade los elementos a otra lista
    mi_lista = [1, 2, 3]
    otra_lista = [4, 5, 6]
    mi_lista.extend(otra_lista)
    print(mi_lista)

    #Inserta un elemento en una posicion especial
    mi_lista = [1, 2,  3]
    mi_lista.insert(1,4)
    print(mi_lista)

    #Elimina el primer elemneto encontradoo
    mi_lista = [1, 2, 3, 2]
    mi_lista.remove(2)
    print(mi_lista)

    #Elimina y devuelve el elemntoo en una
    mi_lista = [1, 2, 3]
    elemento = mi_lista.pop(1)
    print(elemento)
    print(mi_lista)

    #DEvuelve el indice de la primera aparicion
    mi_lista = [1, 2, 3, 2]
    indice = mi_lista.index(2)
    print(indice)

    #Devuelve el numero de veces que aparece un
    mi_lista = [1, 2, 3, 2]
    conteo = mi_lista.count(2)
    print(conteo)

    #Ordena los elementos de la lista de forma acendente
    mi_lista = [3, 1, 4, 2]
    mi_lista.sort()
    print(mi_lista)

    mi_lista.sort(reverse=True)
    print(mi_lista)

    #Invierte el orden de los elementos de la
    mi_lista=[1, 2, 3, 4]
    mi_lista.reverse()
    print(mi_lista)

    #Elimina todos los elementos de la lista
    mi_lista=[1, 2, 3]
    mi_lista.clear()
    print(mi_lista)

   #Devuelve una copia superficial de la lista
    mi_lista=[1, 2, 3]
    mi_lista2=mi_lista
    copia_lista=mi_lista.copy()
    mi_lista.append(4)

    print(copia_lista)
    #print(copia_lista2)
