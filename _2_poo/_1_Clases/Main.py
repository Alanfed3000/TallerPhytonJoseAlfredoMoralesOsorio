class Auto:
    marca="Honda" #Esto es un atributo de la clase Auto
    modelo=1000 #Esto es un atributo de la clase Auto
    placa="PCH-96-04" #Esto es un atributo de la clase Auto

if __name__ == '__main__':
    taxi=Auto() #Esto es una instancia de la clase Archivo
    miauto=Auto() #Esto es otra instancia de la misma clase

    print(taxi.placa) #Se invoca uno de los atributos de la
    miauto.placa="TCV-963-12"
    print(miauto.placa)
    