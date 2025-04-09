class ListaDatos:
    def __init__(self, matricula: str, estudiante: str, asignatura: str):
        self.matricula = matricula
        self.estudiante = estudiante
        self.asignatura = asignatura

if __name__ == '__main__':
    lista=[]

    lista.append(ListaDatos("22240041", "Juan Jesus", "POO"))
    lista.append(ListaDatos("22240051", "Michell", "CIENCIAS"))
    lista.append(ListaDatos("22240067", "Daniela", "PROGRAMACION"))
    lista.append(ListaDatos("22240045", "Alicia", "BD"))

    for obj in lista:
        print(f"Matricula: {obj.matricula}")
        print(f"Nombre: {obj.estudiante}")  # Corrección: usa obj.estudiante en lugar de obj.nombre
        print(f"Asignatura: {obj.asignatura}") #Correccion de ortografia
        print("--------------------------------------")