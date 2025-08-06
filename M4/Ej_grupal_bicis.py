from datetime import datetime

# Excepción personalizada
class ReservaInvalidaError(Exception):
    pass

class Bicicleta:
    ''' Clase que representa una bicicleta en el sistema '''
    def __init__(self, id_bici, modelo):
        self.id_bici = id_bici
        self.modelo = modelo
        self.disponible = True
        self.estado = "buena"

    def __str__(self):
        return f"Bicicleta {self.id_bici} ({self.modelo}) - Estado: {self.estado} - Disponible: {self.disponible}"

class Reserva:
    ''' Clase que representa una reserva de bicicleta '''
    def __init__(self, bicicleta, cliente, hora_inicio, hora_fin):
        # Validaciones de reserva
        if not isinstance(bicicleta, Bicicleta):
            raise ReservaInvalidaError("El objeto bicicleta no es válido.")
        if not bicicleta.disponible:
            raise ReservaInvalidaError(f"La bicicleta {bicicleta.id_bici} no está disponible.")
        if hora_fin <= hora_inicio:
            raise ReservaInvalidaError("La hora de fin debe ser posterior a la hora de inicio.")
        
        self.bicicleta = bicicleta
        self.cliente = cliente
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.costo = self.calcular_costo()

        self.bicicleta.disponible = False

    def calcular_costo(self):
        ''' Calcula el costo de la reserva basado en la duración '''
        duracion = (self.hora_fin - self.hora_inicio).seconds // 3600
        duracion = max(duracion, 1)
        return 1000 * duracion

    def finalizar_reserva(self):
        ''' Finaliza la reserva y libera la bicicleta '''
        self.bicicleta.disponible = True
        print(f"Reserva finalizada para {self.cliente}. Total a pagar: ${self.costo}")

class SistemaReservas:
    ''' Clase que gestiona el sistema de reservas de bicicletas '''
    def __init__(self):
        # Inicializa el sistema con listas para bicicletas y reservas
        self.bicicletas = []
        self.reservas = []

    def registrar_bicicleta(self, id_bici, modelo):
        ''' Registra una nueva bicicleta en el sistema '''
        if any(b.id_bici == id_bici for b in self.bicicletas): # Verifica si la bicicleta ya está registrada
            print(f"Bicicleta con ID {id_bici} ya registrada.")
            return
        bici = Bicicleta(id_bici, modelo)
        self.bicicletas.append(bici)
        print(f"Bicicleta {id_bici} registrada correctamente.")

    def mostrar_bicicletas(self):
        ''' Muestra todas las bicicletas registradas '''
        print("\n=== Lista de Bicicletas Registradas ===")
        if not self.bicicletas:
            print("No hay bicicletas registradas.")
        else:
            for bici in self.bicicletas:
                print(bici)

    def buscar_bicicleta(self, id_bici):
        ''' Busca una bicicleta por su ID '''
        ''' Retorna la bicicleta si se encuentra, o None si no existe '''
        bici = None
        for b in self.bicicletas:
            if b.id_bici == id_bici:
                bici = b
                break
        return bici

    def reservar(self, id_bici, cliente, inicio_str, fin_str):
        ''' Realiza una reserva de bicicleta '''
        ''' Valida las fechas y registra la reserva si es válida '''
        try:
            inicio = datetime.strptime(inicio_str, "%Y-%m-%d %H:%M")
            fin = datetime.strptime(fin_str, "%Y-%m-%d %H:%M")

            bici = self.buscar_bicicleta(id_bici)
            if bici is None:
                raise ReservaInvalidaError("Bicicleta no encontrada.")

            reserva = Reserva(bici, cliente, inicio, fin)
            self.reservas.append(reserva)
            print(f"Reserva realizada correctamente para {cliente}.")
        except ReservaInvalidaError as e:
            print(f"Error de reserva: {e}")
        except ValueError:
            print("Formato de fecha incorrecto. Usa: YYYY-MM-DD HH:MM")
        except Exception as e:
            print(f"Error inesperado: {e}")
        finally:
            print("Intento de reserva procesado.\n")

    def finalizar_reserva(self, cliente):
        ''' Finaliza una reserva activa para un cliente '''
        ''' Busca la reserva y la finaliza si es válida '''
        for reserva in self.reservas:
            if reserva.cliente == cliente and not reserva.bicicleta.disponible:
                reserva.finalizar_reserva()
                return
        print("No se encontró una reserva activa para ese cliente.\n")

# Menú interactivo
def menu():
    ''' Muestra el menú principal del sistema de reservas '''
    print("Bienvenido a BIKECITY - Sistema de Reservas de Bicicletas")
    sistema = SistemaReservas()

    while True:
        print("\n=== MENÚ BIKECITY ===")
        print("1. Registrar bicicleta")
        print("2. Ver bicicletas")
        print("3. Hacer reserva")
        print("4. Finalizar reserva")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_bici = input("ID de la bicicleta: ")
            modelo = input("Modelo: ")
            sistema.registrar_bicicleta(id_bici, modelo)

        elif opcion == "2":
            sistema.mostrar_bicicletas()

        elif opcion == "3":
            id_bici = input("ID de la bicicleta a reservar: ")
            cliente = input("Nombre del cliente: ")
            inicio = input("Hora de inicio (YYYY-MM-DD HH:MM): ")
            fin = input("Hora de fin (YYYY-MM-DD HH:MM): ")
            sistema.reservar(id_bici, cliente, inicio, fin)

        elif opcion == "4":
            cliente = input("Nombre del cliente para finalizar reserva: ")
            sistema.finalizar_reserva(cliente)

        elif opcion == "5":
            print("Gracias por usar BIKECITY.")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__": # Ejecuta el menú al iniciar el script
    print("Iniciando el sistema de reservas...")
    menu()

