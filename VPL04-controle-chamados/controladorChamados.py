from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipos_chamados = []

    def totalChamadosPorTipo(self, tipo: TipoChamado):
        cont_tipo = 0
        for chamado in self.__chamados: 
            if chamado.tipo == tipo: cont_tipo += 1 
        return cont_tipo

    def incluiChamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado):
        if type(cliente) == Cliente and type(tecnico) == Tecnico and type(tipo) == TipoChamado:
            existe = False
            for chamado in self.__chamados:
                if (chamado.data == data and 
                    chamado.cliente.codigo == cliente.codigo and 
                    chamado.tecnico.codigo == tecnico.codigo and 
                    chamado.tipo.codigo == tipo.codigo): 
                    existe = True
                    break
            if not existe:
                novo_chamado = Chamado(data, cliente, tecnico, titulo,
                                       descricao, prioridade, tipo)
                self.__chamados.append(novo_chamado)
                return novo_chamado

    def incluiTipoChamado(self, codigo: int, nome: str, descricao: str):
        existe = False
        for tipo_chamado in self.__tipos_chamados:
            if tipo_chamado.codigo == codigo:
                existe = True
        if not existe:
            novo_tipo_chamado = TipoChamado(codigo, nome, descricao)
            self.__tipos_chamados.append(novo_tipo_chamado)
            return novo_tipo_chamado

    @property
    def tipoChamados(self):
        return self.__tipos_chamados
