if __name__ == '__main__':
    nom1 = input("Proporciona un nombre: ")
    nom2 = input("Proporciona otro nombre: ")

    t1 = len(nom1)
    t2 = len(nom2)

    if t1 > t2:
        print(f"El nombre más largo es: {nom1}")
    elif t2 > t1:
        print(f"El nombre más largo es: {nom2}")
    else:
        print("Ambos nombres tienen la misma longitud.")
