from ave import Ave

class Canarinho(Ave):
  def __init__(self,tamanho_passo:int, altura_voo:int):
    super().__init__(tamanho_passo, altura_voo)
  
  def cantar(self):
    return self.produzir_som() + ' PIU'



canario = Canarinho(1,7)
print(canario.mover())