"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

from typing import List


class Ordenacao():
		def __init__(self, array_para_ordenar:List):
			"""Recebe array com o conteudo a ser ordenado"""
			self.array_to_order = array_para_ordenar
			
		def ordena(self):
			"""Realiza a ordenacao do conteudo do array recebido no construtor"""
			array = self.array_to_order
			new_array = array[:]
			cont_min = 0
			cont_eq = 0
			for item in array:
				for i in array:
					if item > i:
						cont_min += 1
					elif item == i:
						cont_eq += 1
				for x in range(0,cont_eq):
					new_array[cont_min+x] = item
				cont_min = 0
				cont_eq = 0
			return new_array

		def toString(self):
			array = self.ordena()
			"""Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
        """
			string = ''
			for index in range(0, len(array)):
				if index < len(array)-1:
					string += f'{array[index]},'
				else:
					string += f'{array[index]}'
			return string

ordenacao1 = Ordenacao([5,4,2,3,2,3,1])
print(ordenacao1.ordena())