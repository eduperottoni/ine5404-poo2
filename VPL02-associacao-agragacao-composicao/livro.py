from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
  def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
    self.__codigo = codigo
    self.__titulo = titulo
    self.__ano = ano
    self.__editora = editora
    self.__autores = []
    self.__capitulos = []
    self.incluirCapitulo(numeroCapitulo, tituloCapitulo)
    self.incluirAutor(autor)

  @property
  def codigo(self): return self.__codigo
  @property
  def titulo(self): return self.__titulo
  @property
  def ano(self): return self.__ano
  @property
  def editora(self): return self.__editora
  @property
  def autores(self): return self.__autores

  @codigo.setter
  def codigo(self, codigo): self.__codigo = codigo
  @titulo.setter
  def titulo(self, titulo): self.__titulo = titulo
  @ano.setter
  def ano(self, ano): self.__ano = ano
  @editora.setter
  def editora(self, editora: Editora): self.__editora = editora

  def incluirAutor(self, autor: Autor):
    #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
    #Nao permitir insercao de Autores duplicados!
    if type(autor) == Autor and autor not in self.__autores: self.__autores.append(autor)
  
  def excluirAutor(self, autor: Autor): self.__autores.remove(autor)

  def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
    #Nao permitir insercao de Capitulos duplicados!
    cap = Capitulo(numeroCapitulo, tituloCapitulo)
    for capitulo in self.__capitulos:
      if capitulo.titulo == tituloCapitulo: return
    self.__capitulos.append(cap)

  def excluirCapitulo(self, tituloCapitulo: str):
    for capitulo in self.__capitulos:
      if capitulo.titulo == tituloCapitulo: self.__capitulos.remove(capitulo)

  def findCapituloByTitulo(self, tituloCapitulo: str): 
    for capitulo in self.__capitulos:
      if capitulo.titulo == tituloCapitulo: return capitulo
