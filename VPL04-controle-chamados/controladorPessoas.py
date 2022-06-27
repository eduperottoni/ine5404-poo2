from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self):
        return self.__clientes

    @property
    def tecnicos(self):
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str):
        existe = False

        for cliente in self.__clientes:
            if cliente.codigo == codigo:
                existe = True
                break
        if not existe:
            novo_cliente = Cliente(nome, codigo)
            self.__clientes.append(novo_cliente)
            return novo_cliente

    def incluiTecnico(self, codigo: int, nome: str):
        existe = False

        for tecnico in self.__tecnicos:
            if tecnico.codigo == codigo:
                existe = True
                break

        if not existe:
            novo_tecnico = Tecnico(nome, codigo)
            self.__tecnicos.append(novo_tecnico)
            return novo_tecnico
