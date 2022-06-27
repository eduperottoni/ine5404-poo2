from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: float):
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade

    @property
    def nome(self):
        return self.__nome
    
    @property
    def altura(self):
        return self.__altura

    @property
    def comprimento(self):
        return self.__comprimento
    
    @property
    def carga(self):
        return self.__carga
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    def mostrar_nome(self):
        return f'Nome: {self.__nome}'

    @abstractmethod
    def mostrar_detalhes(self):
        string = self.mostrar_nome() + f'Altura: {self.__altura} m\n\
                                         Comprimento: {self.__comprimento} m\n\
                                         Carga: {self.__carga} ton\n\
                                         Velocidade: {self.__velocidade} Km/h'
        return string
