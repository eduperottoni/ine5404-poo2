from classes.transporte import Transporte


class TransporteAquatico(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, boca: float, calado: float):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.boca = boca
        self.calado = calado

    def mostrar_detalhes(self):
        return super().mostrar_detalhes + f'Boca: {self.__boca} m\n\
                                            Calado: {self.__calado} m'