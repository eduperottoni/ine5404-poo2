from classes.transporte import Transporte


class TransporteTerrestre(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float, motor: str, rodas: str):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.motor = motor
        self.rodas = rodas
    
    def mostrar_detalhes(self):
        return super().mostrar_detalhes + f'Motor: {self.__motor}\n\
                                            Rodas: {self.__rodas}'