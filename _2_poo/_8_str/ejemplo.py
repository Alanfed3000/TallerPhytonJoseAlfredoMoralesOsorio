class DatosPersonales:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def getNommbre(self):
        return self.nombre;

    def getApellido(self):
        return self.apellido;

    def getEdad(self):
        return self.edad;

    def corto(self):
        return self.nombre+" "+self.apellido+" "+self.edad+" años";

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.edad+" años";

if __name__ == '__main__':
    datos=DatosPersonales("Emilio", "Candela", "19")
    print(datos)