# EcoViaje_grupoX.py

# Lista de excursiones disponibles con su respectivo cupo máximo
excursiones = {
    1: {"nombre": "Reserva Parque Oncol", "cupo": 3, "reservas": []},
    2: {"nombre": "Parque Nacional Torres del Paine", "cupo": 5, "reservas": []},
    3: {"nombre": "Reserva Natural Huilo Huilo", "cupo": 2, "reservas": []}
}

# Función para mostrar las excursiones y cupos disponibles
def mostrar_excursiones():
    print("\nExcursiones Disponibles:")
    for num, datos in excursiones.items():
        cupos_restantes = datos["cupo"] - len(datos["reservas"])
        print(f"{num}. {datos['nombre']} - Cupos disponibles: {cupos_restantes}")

# Ciclo principal del sistema
while True:
    mostrar_excursiones()

    opcion = input("\nIngresa el número de excursión que deseas reservar (o escribe 'salir' para terminar): ")

    if opcion.lower() == "salir":
        print("\nGracias por usar EcoViaje. Hasta pronto.")
        break

    if not opcion.isdigit():
        print("Opción no válida. Intenta nuevamente.")
        continue

    opcion = int(opcion)

    if opcion not in excursiones:
        print("Número de excursión inválido.")
        continue

    excursion = excursiones[opcion]
    cupos_disponibles = excursion["cupo"] - len(excursion["reservas"])

    if cupos_disponibles <= 0:
        print("Esta excursión ya está llena. Por favor, elige otra.")
        continue

    nombre = input("Ingresa tu nombre para la reserva: ").strip()

    if nombre in excursion["reservas"]:
        print("Ya tienes una reserva en esta excursión.")
        continue

    excursion["reservas"].append(nombre)
    print(f"Reserva confirmada para {nombre} en {excursion['nombre']}.")

# Mostrar resumen final
print("\nResumen de Reservas:")
for num, datos in excursiones.items():
    reservas = ", ".join(datos["reservas"]) if datos["reservas"] else "Sin reservas"
    print(f"{datos['nombre']} ({len(datos['reservas'])}/{datos['cupo']}): {reservas}")
