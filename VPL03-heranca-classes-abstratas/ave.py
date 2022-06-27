from abc import ABC, abstractmethod
from animal import Animal

class Ave(Animal, ABC):
    @abstractmethod
    def __init__(self, tamanho_passo:int, altura_voo:int):
        super().__init__(tamanho_passo)
        self.__altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, altura_voo:int):
        self.__altura_voo = altura_voo
    
    def mover(self):
        return f'ANIMAL: DESLOCOU {self.tamanho_passo} VOANDO'
    
    def produzir_som(self):
        return 'AVE: PRODUZ SOM:'


        

    

