# Sistema de reservas de bicicletas

from datetime import datetime

class ReservaInvalidaError(Exception):
    pass


class Bicicleta:
    '''Clase que representa a una bici'''
    def __init__(self, id_bici, tipo):
        #Valdaciones de Bici
        if not isinstance(id_bici, int) or id_bici <= 0:
            raise ValueError("El ID de la bicicleta debe ser un número entero positivo o un valor válido.")
        self.id_bici = id_bici
        self.tipo = tipo
        self.disponible = True
        self.estado = "buena"
    def __str__(self):
        return f'Bicicleta n° {self.id_bici} del tipo {self.tipo}'

class Reserva:
    '''Clase que representa a una reserva en el sistema'''
    def __init__(self, bicicleta, cliente, hora_inicio, hora_fin):
        # Validaciones de reserva
        if not isinstance(bicicleta, Bicicleta):
            raise ValueError("El objeto bicicleta no es válido.")
        if not bicicleta.disponible:
            raise ValueError(f"La bicicleta {bicicleta.id_bici} no está disponible.")
        if hora_fin <= hora_inicio:
            raise ValueError("La hora de fin debe ser posterior a la hora de inicio.")
        
        self.bicicleta = bicicleta
        self.cliente = cliente
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.costo = self.calcular_costo()

        self.bicicleta.disponible = False

    def calcular_costo(self):
        '''Calcula el costo de la reserva basado en la duración'''
        duracion = (self.hora_fin - self.hora_inicio).seconds
        return duracion * 2
    
class SistemaReservas:
    '''Clase que gestiona el sistema de reservas de bicicletas'''
    def __init__(self):
        self.bicicletas = []
        self.reservas = []

    def registrar_bicicleta(self, id_bici, tipo):
        '''Registra una nueva bicicleta en el sistema'''
        # Verifica si la bicicleta ya está registrada
        if any(b.id_bici == id_bici for b in self.bicicletas):
            print(f"Bicicleta con ID {id_bici} ya registrada.")
            return
        bici = Bicicleta(id_bici, tipo)
        self.bicicletas.append(bici)
        print(f"Bicicleta {bici} registrada exitosamente.")
    
    def reservar_bicicleta(self, id_bici, cliente, hora_inicio, hora_fin):
        '''Realiza una reserva de bicicleta'''

        bicicleta = next((b for b in self.bicicletas if b.id_bici == id_bici), None) # revisa si la bicicleta existe
        if bicicleta is None:
            print(f"Bicicleta con ID {id_bici} no encontrada.")
            return
        try:
            reserva = Reserva(bicicleta, cliente, hora_inicio, hora_fin)
            self.reservas.append(reserva)
            print(f"Reserva realizada: {reserva.bicicleta} para {cliente} desde {hora_inicio} hasta {hora_fin}. Costo: ${reserva.costo}")
        except ValueError as e:
            print(f"Error al realizar la reserva: {e}") 
        except ReservaInvalidaError as e:
            print(f"Error de reserva: {e}")
        finally:
            print("Proceso de reserva finalizado.")

# Menu
def menu():
    print("Sistema de Reservas de Bicicletas")
    print("1. Registrar Bicicleta")
    print("2. Reservar Bicicleta")
    print("3. Salir")
    sistema= SistemaReservas()
    
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            id_bici = int(input("Ingrese ID de la bicicleta: "))
            tipo = input("Ingrese tipo de bicicleta: ")
            sistema.registrar_bicicleta(id_bici, tipo)
        elif opcion == '2':
            id_bici = int(input("Ingrese ID de la bicicleta a reservar: "))
            cliente = input("Ingrese nombre del cliente: ")
            hora_inicio = datetime.strptime(input("Ingrese hora de inicio (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            hora_fin = datetime.strptime(input("Ingrese hora de fin (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            sistema.reservar_bicicleta(id_bici, cliente, hora_inicio, hora_fin)
        elif opcion == '3':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    print("Cargando el sistema de reservas de bicicletas...")
    menu()    