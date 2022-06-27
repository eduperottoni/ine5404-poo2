from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


'''
O calculo da Aliquota do ISS (percentual do imposto) leva
em conta a lista de Servicos
Para cada servico cadastrado na lista de Servicos do ISS,
eh reduzido 0,1 da Aliquota.
Por exemplo, se a aliquota informada no construtor for 10.0 e
tiverem sido incluidos 2 servicos na lista,
entao a aliquota calculada sera de 9.8
'''


class ISS(Imposto):
    def __init__(self, aliquota: float, incidencia_imposto: IncidenciaImposto):
        super().__init__(aliquota, incidencia_imposto)
        self.__servicos = []

    def inclui_servico(self, nome: str):
        if nome not in self.__servicos:
            self.__servicos.append(nome)

    def exclui_servico(self, nome: str):
        self.__servicos.remove(nome)

    def calcula_aliquota(self):
        return self.aliquota - len(self.__servicos) * 0.1
