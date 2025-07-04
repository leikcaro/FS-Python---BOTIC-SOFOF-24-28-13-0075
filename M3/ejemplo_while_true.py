#El sistema debe poder ingresar estudiantes y su edad
#Debe poder mostrar los estudiantes que existen
#Buscar a los estudiantes por nombre
#Ordenar a los estudiantes por edad

estudiantes = {}

def menu():

    print("Bienvenido al sistema de gestión de Estudiantes")
    while True:
        
        print("\n ----- Menú de registro de estudiantes -----")
        print("Opción 1: Registrar un estudiante")
        print("Opción 2: Listar estudiantes")
        opcion =input("Seleccione una opción entre 1 y 6: ")

        if opcion=="1":
            print("Ingrese el nombre y la edad del estudiante:")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            estudiantes[nombre]= edad

        if opcion=="2":
            print("Los estudiantes son:\n")
            print(estudiantes)
            print(estudiantes.keys())
            print(estudiantes.values())
        
        if opcion=="3":
            pass

        elif opcion=="6":
            print("Gracias por usar el sistema de gestion de Estudiantes")
            break

menu()