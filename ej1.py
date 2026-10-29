notas = {
    "Gomez": [],
    "Rodriguez": [],
    "Fernandez": [],
    "Lopez": [],
    "Martinez": []
}
while True:
    print("- - - - - - - - - - - - - -")
    print("|     SISTEMA DE NOTAS    |")
    print("- - - - - - - - - - - - - -")
    print("1.Ver todas las notas")
    print("2.Ver notas por alumno")
    print("3.Cargar notas")
    print("4.Promedio")
    print("5.Salir")
    op = input()
    if op == "1":
        for x in notas:
            print(x, ".", notas[x])
    elif op == "2":
        al = input("Apellido: ")
        if al in notas:
            print(notas[al])
        else:
            print("Ese alumno no existe")
    elif op == "3":
        al = input("Apellido: ")
        if al in notas:
            print("Nota 1")
            n1 = int(input())
            print("Nota 2")
            n2 = int(input())
            print("Nota 3")
            n3 = int(input())
            print("Nota 4")
            n4 = int(input())
            print("Nota 5")
            n5 = int(input())
            notas[al] = [n1, n2, n3, n4, n5]
            print("Notas cargadas")
        else:
            print("Ese alumno no existe")
    elif op == "4":
        al = input("Apellido: ")
        if al in notas:
            lista = notas[al]
            if len(lista) == 0:
                print("No tiene notas cargadas")
            else:
                suma = lista + lista + lista + lista + lista
                prom = suma / 5
                print("Promedio:", prom)
        else:
            print("Ese alumno no existe")
    elif op == "5":
        break



