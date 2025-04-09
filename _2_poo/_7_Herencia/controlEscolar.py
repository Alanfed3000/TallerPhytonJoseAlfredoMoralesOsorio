class ListaDatos:
    def _init_(self,matricula:str,estudiante:str,asignatura:str):
        self.matricula=matricula
        self.estudiante=estudiante
        self.asignatura=asignatura

class ControlEscolar(ListaDatos):

    def _init_(self):
        self.lista=[]

    def addestudiante(self, matricula, estudiante, asignatura):
        self.lista.append(ListaDatos(matricula, estudiante, asignatura))

    def show(self):
        for datos in self.lista:
            print(f'matricula: {datos.matricula}')
            print(f'estudiante: {datos.estudiante}')
            print(f'asignatura: {datos.asignatura}')
            print('------------------------------------')

if __name__ == '__main__':
    escolar=ControlEscolar()
    escolar.addEstudiante("123456", "jose perez", "POO")
    escolar.addEstudiante('2223002', 'mariana mendez', 'Est-datos')
    escolar.show()