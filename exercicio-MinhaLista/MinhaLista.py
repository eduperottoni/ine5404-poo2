class MinhaLista:
	'''MinhaLista cria MinhaListas a partir de outros built-ins types: 
	(inteiros, floats, strings, listas, tuplas, sets). No caso das estruturas
	compostas (listas, tuplas e sets), MinhaLista converte essa estrutura para o tipo MinhaLista'''
	def __init__(self, *params):
		if (len(params) == 1 and type(*params) in [list, tuple, set]):
			self.__tuple = tuple(item for item in params[0])
		else:
			self.__tuple = (params)

	def soma(x, y):
		return x+y
	
	def __sliceTupleByIndex(self, index:int):
		'''__sliceTupleByIndex() separa uma tupla em três partes e as retorna.
		A primeira parte é a que vem antes do índice. A parte selecionada
		é o que está no índice e a última parte, o que vem depois do índice'''
		first_part = self.__tuple[:index]
		selected_part = self.__tuple[index]
		last_part = self.__tuple[index+1:]
		if index == -1:
			last_part = tuple()
		return (first_part, selected_part, last_part)

	def __orderVector(self, reverse = False):
		'''Algoritmo de ordenação (aproveitado do exercício de Ordenação)'''
		strings = 0
		numbers = 0
		for item in self.__tuple:
			if type(item) == str:
				strings += 1
			elif type(item) == int or type(item) == float:
				numbers += 1
		if (strings == 0 and numbers > 0) or (strings > 0 and numbers == 0):
			old_tuple = self.__tuple[:]
			new_tuple = old_tuple[:]
			cont_minormax = 0
			cont_eq = 0
			for item in old_tuple:
				for i in old_tuple:
					if reverse:
						if item < i:
							cont_minormax += 1
						elif item == i:
							cont_eq += 1
					else:
						if item > i:
							cont_minormax += 1
						elif item == i:
							cont_eq += 1
				for x in range(0,cont_eq):
					first_part, selected_part, last_part = MinhaLista(new_tuple).__sliceTupleByIndex(cont_minormax+x)
					new_tuple = first_part + (item,) + last_part
				cont_minormax = 0
				cont_eq = 0
			return new_tuple

	#Indexer Operator | Acesso
	def __getitem__(self, index : int):
		for tuple_index, item in enumerate(self.__tuple):
			if tuple_index == index:
				return self.__tuple[index]

	#Atribuição a item da MinhaLista
	def __setitem__(self, index : int, value):
		first_part, selected_part, last_part = self.__sliceTupleByIndex(index)
		self.__tuple = first_part + (value,) + last_part

	#Print (usa a notação de lista)
	def __str__(self):
		#return f'{[item for item in self.__tuple]}'
		string = ""
		for  index, item in enumerate(self.__tuple):
			if (type(item) == MinhaLista):
				string += str(item)
			elif (type(item) == str):
				string += f"'{(item)}'"
			else:
				string += f'{item}'
			if (index < len(self.__tuple) - 1):
				string += ', '
		return f'[{string}]'

	#len da MinhaLista
	def __len__(self):
		cont = 0
		for item in self.__tuple:
			cont += 1
		return cont
			
	def append(self, element):
		'''MinhaLista.append() | Adiciona elemento na última posição de MinhasListas'''
		newElement = (element,)
		self.__tuple = self.__tuple + newElement

	def pop(self, index : int = -1):
		'''MinhaLista.pop() | remove o que estiver no índice passado por parâmetro e o retorna.
		Caso o índice não for passado, remove o último elemento (índice = -1)'''
		first_part, selected_part, last_part = self.__sliceTupleByIndex(index)	
		self.__tuple = (first_part + last_part)
		return selected_part

	def remove(self, element):
		'''MinhaLista.remove() | remove a primeira ocorrência do elemento passado como parâmetro'''
		for index, item in enumerate(self.__tuple):
			if item == element:
				first_part, selected_part, last_part = self.__sliceTupleByIndex(index)
				self.__tuple = (first_part + last_part)
				break
				
	def sort(self, reverse = False):
		'''MinhaLista.sort() | Ordena os elementos da lista se todos
		forem números ou strings. Parâmetro opcional reverse diz se a ordenação 
		é ou não decrescente'''
		self.__tuple = self.__orderVector()

	def reverse(self):
		'''MinhaLista.reverse() | Reverte os elementos da MinhaLista. Ou seja, quem estava no
		índice zero troca com o índice len(self)-1, quem estava em penúltimo, troca com o segundo
		lugar e assim por diante...'''
		self.__tuple = self.__tuple[::-1]

	def __add__(self, otherMinhaLista):
		'''Define o operador + para MinhaListas'''
		if (type(otherMinhaLista) == MinhaLista):
			return MinhaLista(self.__tuple + otherMinhaLista.__tuple)

	def __mul__(self, integer):
		if (type(integer) == int):
			return MinhaLista(self.__tuple * integer)


#####################################################
#TESTES DOS MÉTODOS TRABALHADOS NA CLASSE MINHALISTA

lista1 = MinhaLista(1,5,3,4,5,1,10,8,9)
lista2 = MinhaLista(5)
lista3 = MinhaLista('teste', 'oi', 'abc', 'zyed')
lista4 = MinhaLista((1,2,3,4,5))
lista5 = MinhaLista({1,2,3,4,2,1,5})
lista6 = MinhaLista(1.5)
lista7 = MinhaLista()
lista8 = MinhaLista([1,2,3,4,5, 3, 4, 5, 8])
lista9 = MinhaLista(lista4, [1,2], 2, 6.7, 'oi', {1,2,3}, (8,5,2))
lista10 = MinhaLista(lista1)

lista_teste = MinhaLista('edu',5)

lista_de_MinhaListas = [lista1, lista2, lista3, lista4, lista5, lista6, lista7, lista8, lista9, lista10]

print('TESTE DO PRINT')
for index, MinhaLista_item in enumerate(lista_de_MinhaListas):
	print(f'{index+1} | MinhaLista obj=> {MinhaLista_item}')
print('-'*40)

print('TESTE DO OPERADOR DE ACESSO []')
for index, MinhaLista_item in enumerate(lista_de_MinhaListas):
	print(f'{index+1} | MinhaLista obj[0] => {MinhaLista_item[0]}')
print('-'*40)

print('TESTE DO LEN')
for index, MinhaLista_item in enumerate(lista_de_MinhaListas):
	print(f'{index+1} | len => {len(MinhaLista_item)}')
print('-'*40)

print('TESTE DO SORT')
for index, MinhaLista_item in enumerate(lista_de_MinhaListas):
	if index in [0, 2, 4, 7]:
		print(f'MinhaLista {index +1} pre-sorts: {MinhaLista_item}')
		MinhaLista_item.sort()
		print(f'|MinhaLista {index+1} pos-sort : {MinhaLista_item}')
print('-'*40)

print('TESTE DO REVERSE')
for index, MinhaLista_item in enumerate(lista_de_MinhaListas):
	print(f'MinhaLista {index +1} pre-reverse: {MinhaLista_item}')
	MinhaLista_item.reverse()
	print(f'|MinhaLista {index+1} pos-reverse : {MinhaLista_item}')
print('-'*40)

print('TESTE DE +')
for index, MinhaLista_item in enumerate(lista_de_MinhaListas):
	print(f'|{MinhaLista_item} + {lista_teste} = {MinhaLista_item + lista_teste}')
print('-'*40)

print('TESTE DE *')
for index, MinhaLista_item in enumerate(lista_de_MinhaListas):
	print(f'|{MinhaLista_item} * {3} = {MinhaLista_item * 5}')
print('-'*40)

print('TESTE DO APPEND')
for index, MinhaLista_item in enumerate(lista_de_MinhaListas):
	print(f'{index+1} | MinhaLista obj inicial => {MinhaLista_item}')
	MinhaLista_item.append('string')
	MinhaLista_item.append([1,2])
	MinhaLista_item.append((1,2))
	MinhaLista_item.append({1,2})
	MinhaLista_item.append(lista_teste)
	print(f'{index+1} | MinhaLista obj final => {MinhaLista_item}')
print('-'*40)

print('TESTE DE ATRIBUICAO')
for index, MinhaLista_item in enumerate(lista_de_MinhaListas):
	MinhaLista_item[-2] = 'Eduardo'
	print(f'| {index+1} => {MinhaLista_item}')
print('-'*40)

print('TESTE DO POP')
for index, MinhaLista_item in enumerate(lista_de_MinhaListas):
	print(f'Lista {index+1} pre-remocao: {MinhaLista_item}')
	print(f'Tamanho => {len(MinhaLista_item)}')
	print(f'| pop() => removido: {MinhaLista_item.pop()}')
	print(f'Lista {index+1} pos-remocao: {MinhaLista_item}')
	print(f'Tamanho => {len(MinhaLista_item)}')
print('-'*40)

print('TESTE DO REMOVE')
for index, MinhaLista_item in enumerate(lista_de_MinhaListas):
	print(f'Lista {index+1} pre-remocao: {MinhaLista_item}')
	print(f'Tamanho => {len(MinhaLista_item)}')
	print(f'| remove() => removido: string')
	MinhaLista_item.remove('string')
	print(f'Lista {index+1} pos-remocao: {MinhaLista_item}')
	print(f'Tamanho => {len(MinhaLista_item)}')
print('-'*40)
