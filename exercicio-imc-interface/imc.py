class Imc:
    def __init__(self, peso, altura):
        self.__peso = peso
        self.__altura = altura

    def calcular_imc(self):
        return round(float(self.__peso)/float(self.__altura)**2,2)

    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return 'ABAIXO DO PESO'
        elif 18.5 <= imc < 25:
            return 'PESO NORMAL'
        elif 25 <= imc < 30:
            return 'SOBREPESO'
        elif 30 <= imc < 35:
            return 'OBESIDADE (GRAU I)'
        elif 35 <= imc < 40:
            return 'OBESIDADE SEVERA (GRAU II)'
        else:
            return  'OBESIDADE MÓRBIDA (GRAU III)'

    def validar_entradas(self):
        if not self.__peso.replace('.','').isdigit() or float(self.__peso) < 0 or not self.__altura.replace('.','').isdigit() or float(self.__altura) < 0:
            return False
        else:
            return True