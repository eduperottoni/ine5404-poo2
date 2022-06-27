from imposto import Imposto
from incidencia_imposto import IncidenciaImposto

'''
O calculo da Aliquota do ICMS (percentual do imposto)
leva em conta a "diferenca_estado".
O valor de "diferenca_estado" deve ser somado a aliquota informada.
Por exemplo, se a aliquota informada no construtor for 10.0
e a "diferenca_estado" for 2, entao a aliquota calculada sera de 12.0
'''


class ICMS(Imposto):
    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto,
                 diferenca_estado: float):
        super().__init__(aliquota, incidencia_imposto)
        self.__diferenca_estado = diferenca_estado

    @property
    def diferenca_estado(self):
        return self.__diferenca_estado

    @diferenca_estado.setter
    def diferenca_estado(self, diferenca_estado: float):
        self.__diferenca_estado = diferenca_estado

    def calcula_aliquota(self):
        return self.aliquota + self.__diferenca_estado
