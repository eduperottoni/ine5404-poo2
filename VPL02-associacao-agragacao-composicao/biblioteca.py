from livro import Livro

class Biblioteca:
  def __init__(self, ):
    self.__livros = []

  def incluirLivro(self, livro: Livro):
    #Nao esqueca de garantir que o objeto recebido pertence a classe Livro...
    if type(livro) == Livro and livro not in self.__livros: self.__livros.append(livro)

  def excluirLivro(self, livro: Livro): 
    if livro in self.__livros: self.__livros.remove(livro)

  @property
  def livros(self): return self.__livros