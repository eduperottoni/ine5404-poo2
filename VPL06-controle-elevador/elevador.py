from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        self.__andarAtual = andarAtual
        self.__totalAndaresPredio = totalAndaresPredio
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas

    
    def descer(self) -> str:
    	if self.__andarAtual == 0:
    	    raise ElevadorJahNoTerreoException
    	self.__andarAtual -= 1
    
    
    def entraPessoa(self) -> str:
    	if self.__totalPessoas == self.__capacidade:
    	    raise ElevadorCheioException
    	self.__totalPessoas += 1
    
   
    def saiPessoa(self) -> str:
    	if self.__totalPessoas == 0:
    	    raise ElevadorJahVazioException
    	self.__totalPessoas -= 1
    
    
    def subir(self) -> str:
    	if self.__andarAtual == self.__totalAndaresPredio - 1:
    	    raise ElevadorJahNoUltimoAndarException
    	self.__andarAtual += 1
    
    @property
    def capacidade(self) -> int:
    	return self.__capacidade
    
    @property
    def totalPessoas(self) -> int:
    	return self.__totalPessoas
    
    @property
    def totalAndaresPredio(self) -> int:
        return self.__totalAndaresPredio	
        
    @property
    def andarAtual(self) -> int:
    	return self.__andarAtual
    
    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
    	self.__totalAndaresPredio = totalAndaresPredio
