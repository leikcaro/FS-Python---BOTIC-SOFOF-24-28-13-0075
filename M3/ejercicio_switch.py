"""# Desafío  Coordenadas, Diccionarios y Sets
Vamos a simular un pequeño sistema de registro de puntos en un mapa. Cada punto tendrá un nombre asociado y estará representado por una coordenada '(x, y)'.

## Instrucciones
1. Crear un diccionario vacío llamado 'puntos' que almacenará los datos ingresados.
2. Mostrar un menú con las siguientes opciones, dentro de un ciclo 'while':
   - **1**. Ingresar nueva coordenada (nombre, x, y)
   - **2**. Mostrar todos los puntos guardados
   - **3**. Mostrar el conjunto de nombres únicos (usando un 'set')
   - **4**. Eliminar un punto por su nombre
   - **5**. Salir del programa
3. Utilizar 'match-case' (o 'if-elif' si usas Python < 3.10) para manejar cada opción.
4. Las coordenadas deben guardarse como **tuplas**, por ejemplo: '(3.5, -2.1)'
5. Validar que los valores de las coordenadas sean números reales (float).
6. Cuando el usuario elija salir, finalizar el programa con un mensaje de despedida.

"""

puntos={
    
}
print("Bienvenido a Sistema de Registro de Puntos: ")

while True:
    print("\n Ingrese una de las siguientes opciones: \n")
    print("**1**. Ingresar nueva coordenada (nombre, x, y)")
    print("**2**. Mostrar todos los puntos guardados")
    print("**3**. Mostrar el conjunto de coordenadas únicas (usando un 'set')")
    print("**4**. Eliminar un punto por su nombre")
    print("**5**. Salir del programa")
    
    opcion_elegida=input( "\n Ingresa una opción válida: \n")
    
    match opcion_elegida:
        
        case "5":
            print("Gracias por venir ")
            break
        case "1":
            print(" Ingrese una nueva coordenada. (nombre, x, y) ")
          
            nombre=input("Ingrese el Nombre: \n")
            coordenada_x=float(input("Ingrese la coordenada X : \n"))
            coordenada_y=float(input("Ingrese la coordenada Y : \n"))
            puntos[nombre]=(coordenada_x,coordenada_y)
            
        case "2":
            print(f"Los puntos actuales son:{puntos}")
            
        case "3":
            print("Las coordenadas únicas son:  ")
            print(set(puntos.values()))
        
        case "4":
            borrar=input("Qué punto quieres eliminar? \n")
            del puntos[borrar]
        case _:
            print("Opción inválida. Intente Nuevamente. ")
            #break
        