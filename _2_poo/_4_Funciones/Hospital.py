class Hospital:
    def __init__(self):
        self.__NombrePaciente:str="Federico"
        self.__nss:int=1258
        self.__enfermedad:str=""

    def getNombrePaciente(self)->str:
        return self.__NombrePaciente

    def getNss(self)->int:
        return  self.__nss

    #@property # Esto convierte el metodo en una propiedad de solo lectura
    def getEnfermedad(self)->str:
        # Realizar operaciones
        return self.__enfermedad

    def setNombrePaciente(self, nombre:str):
        self.NombrePaciente=nombre


    def setNss(self,nss:int):
        self.nss=nss

    def setEnfermedad(self, enfermedad:str):
        self.enfermedad=enfermedad

if __name__ == '__main__':
    hospital=Hospital();

    hospital.__NombrePaciente="Juan"

    print(hospital.getNombrePaciente)

    hospital.getNombrePaciente()

    #hospital.setEnfermedad("Gripa")
    #e=hospital.getEnfermedad

    #print(e)