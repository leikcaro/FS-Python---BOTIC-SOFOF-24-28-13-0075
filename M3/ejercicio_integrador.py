# Partir por la creacion de un dict vacío, e
# El while True para mantenernos siempre ejecutando y 
# definir opcion 6 de salir como primer elemento con el break 


estudiantes = {}
def menu():
    while True:
        print("\n=== MENÚ DEL REGISTRO DE ESTUDIANTES ===")
        print("1. Registrar nuevo estudiante")
        print("2. Ver estudiantes registrados")
        print("3. Buscar estudiante por nombre")
        print("4. Eliminar un estudiante")
        print("5. Reporte de edades")
        print("6. Salir")
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ").strip().title()
            if nombre in estudiantes:
                print("Ese estudiante ya está registrado.")
            else:
                try:
                    edad = int(input("Edad del estudiante: "))
                    estudiantes[nombre] = edad
                    print(f"Estudiante {nombre} registrado con éxito.")
                except ValueError:
                    print("Edad inválida. Debe ser un número entero.")

        elif opcion == "2":
            if estudiantes:
                print("\nListado de estudiantes:")
                for nombre, edad in estudiantes.items():
                    print(f"- {nombre}: {edad} años")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "3":
            nombre = input("Nombre del estudiante a buscar: ").strip().title()
            if nombre in estudiantes:
                print(f"{nombre} tiene {estudiantes[nombre]} años.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del estudiante a eliminar: ").strip().title()
            if nombre in estudiantes:
                del estudiantes[nombre]
                print(f"{nombre} ha sido eliminado del registro.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "5":
            if estudiantes:
                edades = list(estudiantes.values())
                promedio = sum(edades) / len(edades)
                print(f"Promedio de edad: {promedio:.2f} años.")
                print("Estudiantes mayores de edad:")
                for nombre, edad in estudiantes.items():
                    if edad >= 18:
                        print(f"- {nombre} ({edad} años)")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "6":
            print("¡Gracias por usar el registro de estudiantes!")
            break
        else:
            print("Opción inválida. Por favor elige entre 1 y 6.")

menu()