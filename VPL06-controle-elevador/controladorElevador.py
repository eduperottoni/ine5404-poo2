from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    
    def subir(self) -> str:
        self.__elevador.subir()
    

    def descer(self) -> str:
        self.__elevador.descer()


    def entraPessoa(self) -> str:
        self.__elevador.entraPessoa()
        

    def saiPessoa(self) -> str:
        self.__elevador.saiPessoa()
	

    @property
    def elevador(self):
    	return self.__elevador


    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        args = [andarAtual, totalAndaresPredio, capacidade, totalPessoas]
        
        for i in args:
            if (not isinstance(i, int) or i<0):
                raise ComandoInvalidoException
                return
                
        if andarAtual > totalAndaresPredio - 1 or totalPessoas > capacidade:
            raise ComandoInvalidoException
            return
        
        self.__elevador = Elevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)
