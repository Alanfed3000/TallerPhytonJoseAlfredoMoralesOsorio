def extras(agenda:tuple):
    i:int=0
    while (i<len(agenda)):
        nombre,correo,tel = agenda[i]
        i+=1
        yield nombre,correo,tel

if __name__ == '__main__':
    agenda=[]

    agenda.append(["Juan","juan@gmail.com","2481312968"])
    agenda.append(["Itzel","juan@gmail.com","2481103051"])
    agenda.append(["Romina","juan@gmail.com","2482086297"])
    agenda.append(["Carlos","juan@gmail.com","2468076267"])
    agenda.append(["Julieta","juan@gmail.com","245777456"])
    agenda.append(["Valeria","juan@gmail.com","2468714978"])
    agenda.append(["Tomas","juan@gmail.com","1234567890"])
    agenda.append(["Ivan","juan@gmail.com","0987654321"])
    agenda.append(["Vanesa","juan@gmail.com","2481188256"])
    agenda.append(["Leonardo","juan@gmail.com","2461236789"])

    for nombre, correo, tel in extras(agenda):
        print(f"Nombre: {nombre}, Correo: {correo}, Teléfono: {tel}")
