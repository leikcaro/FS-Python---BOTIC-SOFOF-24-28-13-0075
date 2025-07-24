'''Crear una aplicación que permita al usuario agregar tareas, verlas, marcarlas 
como completadas y eliminarlas. Además, las tareas deberán guardarse 
en un archivo para que no se pierdan cuando se cierre el programa.'''

#abrir el archivo
#menu con while true

    #match case con opciones:
        # paso 0: Print de menu
        # 1. agregar tarea
        # 2. ver tareas 
        # 3. marcar completada
        # 4. eliminar tarea
        # 5 salir (al salir se guarda la tarea)

tareas=[{"descripcion": "tarea ejemplo", "estado": "pendiente"}]
print("----------------Bienvenido al gestor de Tareas--------------- ")

while True:
    opcion = input("\nIngrese una opción:        \n"
    "\n 1. agregar tarea " \
    "\n 2. ver tareas " \
    "\n 3. marcar completada " \
    "\n 4. eliminar tarea " \
"\n 5. salir (al salir se guarda la tarea) \n")
    
    match opcion:

        case 1:
            agregar_tarea()
        case 2:
            ver_tareas()
        case 3:
            marcar_completadas()
        case 4:
            eliminar_tarea()  
        case 5:
            guardar_tarea()
            break
        case _ :
            print("Opción no válida, intente nuevamente")






#abrir el archivo
#si el archivo "tareas.txt" existe, se abre, si no existe, se crea
with open("tareas.txt", "a") as f:
    f.write("\nWoops! I have deleted the content!!!!!!")

#open and read the file after the overwriting:
with open("tareas.txt") as f:
    print(f.read())