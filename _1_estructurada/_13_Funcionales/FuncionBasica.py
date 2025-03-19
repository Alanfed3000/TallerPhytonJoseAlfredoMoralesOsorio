def suma(a:int,b:int)->int:
    return a+b

def sumaArreglo(lista:list)->int:
    return sum(lista)

if __name__ == '__main__':
    print(f"la suma es {suma(15,22)}")

    print(f"la suma del arreglo es {sumaArreglo([5,6,8,9,7])}")