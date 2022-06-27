from abc import ABC, abstractmethod
from animal import Animal

class Mamifero(Animal, ABC):
    @abstractmethod
    def __init__(self, volume_som:int, tamanho_passo:int):
        super().__init__(tamanho_passo)
        self.__volume_som = volume_som

    @property
    def volume_som(self):
        return self.__volume_som

    @volume_som.setter
    def volume_som(self, volume_som:int):
        self.__volume_som = volume_som

    def produzir_som(self):
        return f'MAMIFERO: PRODUZ SOM: {self.volume_som} '

