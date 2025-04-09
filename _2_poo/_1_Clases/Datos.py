class Datos:
    def __init__(self, nombre, correo, whatsapp):
        self.nombre = nombre
        self.correo = correo
        self.whatsapp = whatsapp

    def setNombre(self, nombre:str):
        self.nombre=nombre

if __name__ == '__main__':
    datos=Datos('Alfredo','josealfredom502@gmail.com', '2481312968')

    print(datos.nombre)
    datos.setNombre("Pablo")
    print(datos.nombre)
    datos.nombre="Gabriel"
    print(datos.nombre)
