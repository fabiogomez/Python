class Lavadora:
    def __init__(self):
        pass
    def lavar(self, temperatura):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print("Llenando el tanque de agua")

    def _anadir_jabon(self):
        print("Anadiendo jabon")
    
    def _lavar(self):
        print("Lavando")
    
    def _centrifugar(self):
        print("Centrifugando")

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar(30)
            