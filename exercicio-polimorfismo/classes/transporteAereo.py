from classes.transporte import Transporte

class TransporteAereo(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, autonomia: float, envergadura: float):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.autonomia = autonomia
        self.envergadura = envergadura

    def mostrar_detalhes(self):
        return super().mostrar_detalhes + f'Autonomia: {self.__autonomia} Km\n\
                                            Evergadura: {self.__envergadura} m'
