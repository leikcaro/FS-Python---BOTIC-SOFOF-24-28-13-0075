class TarjetaCredito:
    def __init__(self, saldo, cupo, tasa):
        self.saldo = saldo
        self.cupo = cupo
        self.tasa = tasa
    def __str__(self):
        return f'Esta tarjeta tiene {self.saldo} de deuda'

class Usuario:


    def __init__(self, nombre, apellido, email):

        self.nombre = nombre

        self.apellido = apellido

        self.email = email

        self.tarjeta = TarjetaCredito(0, 20000, 0.015) #Agregamos esta línea
    
    def __str__(self):

        return f'El cliente {self.nombre} {self.apellido}'

julio = Usuario("Julio", "Palma", "jpalma@skillnest.com")
tarjeta_1 = TarjetaCredito(0, 30000, 0.015)
print("la tarjeta: ", tarjeta_1)
print(julio, "tiene una tarjeta: ", julio.tarjeta)