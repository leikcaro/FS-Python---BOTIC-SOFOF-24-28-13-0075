class Animal:

    def __init__(self, nombre= "gato", edad= 1, color="plomo"):

        self.nombre = nombre

        self.edad = edad

        self.color = color

    def hacer_truco(self):

        print(f"{self.nombre} realiza un truco")


class Gato(Animal):


    def __init__(self, tipo_pelaje, nombre, edad, color):

        super().__init__(nombre, edad, color)
        self.tipo_pelaje = tipo_pelaje

    def __str__(self):
        return f"mi gatito {self.nombre}"

    def razcar_sofa(self):

        print(f'{self.nombre} está razcando el sofá de su casa')


blue = Gato("Corto","Blue", 2, "Blanco")

print(f"La edad de {blue} es: ", blue.edad)

print ("¿Blue es un gato? ", isinstance(blue, Gato))
print ("¿Blue es un animal? ", isinstance(blue, Animal))