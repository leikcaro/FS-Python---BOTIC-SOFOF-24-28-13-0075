class Animal:

    def __init__(self, nombre, edad, color):

        self.nombre = nombre

        self.edad = edad

        self.color = color

    def hacer_truco(self):

        print(f"{self.nombre} realiza un truco")

class Gato(Animal):

    def __init__(self, nombre, edad, color, tipo_pelaje):

        super().__init__(nombre, edad, color)

        self.tipo_pelaje = tipo_pelaje

    def hacer_truco(self):

        print(f"{self.nombre} te ignora un momento")

        print(f"{self.nombre} se rehúsa a hacer el truco")

unicornio = Animal("Azulito", 0, "arcoris")

miu = Gato("Miu", 5, "blanca", "largo")

unicornio.hacer_truco()

miu.hacer_truco()