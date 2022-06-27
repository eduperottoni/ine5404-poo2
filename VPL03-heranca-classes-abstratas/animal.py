from abc import ABC, abstractmethod

class Animal(ABC):
	def __init__(self, tamanhoPasso: int):
		self.__tamanhoPasso = tamanhoPasso

	@property
	def tamanho_passo(self):
		return self.__tamanhoPasso

	@tamanho_passo.setter
	def tamanho_passo(self, tamanho_passo:int):
		self.__tamanhoPasso = tamanho_passo
	
	@abstractmethod
	def produzir_som(self):
		pass
	
	def mover(self):
		return f'ANIMAL: DESLOCOU {self.__tamanhoPasso}'
	
