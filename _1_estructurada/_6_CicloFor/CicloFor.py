import sys
# import sys
# from os.path import split
# from os.path import join

if __name__ == '__main__':
    print("Rango de 0 a 9")
    for i in range(10):
        print(f"{i}")

    print("Rango de 6 a 11")
    for i in range(6,12):
        print(f"{i}")

    print("Rango de 6 a 11 pero con incrementos de ")
    for i in range(6,12,3):
        print(f"{i}", end= " ")

    sys.stdoud.write("Texto sin salto de linea")
    print("-----------------")