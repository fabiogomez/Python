class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def avanzar(self):
        print("ando caminando")

class Ciclista(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def avanzar(self):
        print("ando en bicicleta")

if __name__ == "__main__":
    persona = Persona("Juan", 30)
    persona.avanzar()
    ciclista = Ciclista("Pedro", 25)
    ciclista.avanzar()



    
