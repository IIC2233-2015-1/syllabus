
if __name__=='__main__':
    lista_espacios = []
    lista_espacios.append(SalaDeClases(5, 20, 25, 6))
    lista_espacios.append(SalaDeClases(3, 10, 10, 6))
    lista_espacios.append(SalaDeReuniones(10, 15, 30, 10))
    lista_espacios.append(Subterraneo(20, 20, 40))
    print(lista_espacios[0] == lista_espacios[1])
    print(lista_espacios[0] > lista_espacios[2])
    print(lista_espacios[0] > lista_espacios[3])
    print(lista_espacios[0] < lista_espacios[3])
    print(lista_espacios[3] > lista_espacios[0])
    lista_espacios.append(lista_espacios[0] + lista_espacios[1])
    lista_espacios.append(lista_espacios[0] + lista_espacios[2])
    lista_espacios.append(lista_espacios[2] + lista_espacios[2])
    lista_espacios.append(lista_espacios[3] + lista_espacios[3])

    personas = []
    personas.append(Alumno("Belen"))
    personas.append(Alumno("Patricio"))
    personas.append(Alumno("Jaime"))
    personas.append(Alumno("Marco"))
    personas.append(Alumno("Rodrigo"))
    personas.append(Profesor("Karim"))
    personas.append(Profesor("Christian"))
    personas.append(Profesor("Extra"))
    for p in personas:
        p.entrar_a_sala(lista_espacios[1])
