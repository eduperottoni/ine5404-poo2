from classes.transporte import Transporte
from classes.transporteTerrestre import TransporteTerrestre
from classes.transporteAereo import TransporteAereo
from classes.transporteAquatico import TransporteAquatico

class Catalogo:
    #recebe lista com as instancias dos tipos e uma lista com as classes dos tipos
    def __init__(self, nome: str, lista_transportes: list):
        '''Verifica se os objetos e classes recebidos estão corretos, 
        para compor um controler com atributos consistentes'''
        self.__nome = nome
        self.__tipos_transportes = {1 : ('Transporte Terrestre', TransporteTerrestre), 
                                    2 : ('Transporte Aquático', TransporteAquatico), 
                                    3 : ('Transporte Aéreo' , TransporteAereo)}

        self.__acoes = {1 : ('Inserir Transporte',),
                        2 : ('Ver transportes',)}                            
        
        self.__transportes = []
        for transporte in lista_transportes:
            if isinstance(transporte, Transporte):
                self.__transportes.append(transporte)
        
        self.__acao = ''
        self.__tipo_transporte = ''


    def __boas_vindas(self):
        print('-'*10)
        print(f'Seja bem-vindo ao {self.__nome}!')
        print('-'*10)

    def __despedida(self):
        print('Tchau! Obrigado por utilizar nossos serviços!')

    def __print_menu(self, title :str, dict: dict):
        print(f'---- ESCOLHA {title} ----')
        for key, value in dict.items():
            print(f'[{key}] {value[0]}')
        print('[ENTER PARA SAIR]')


    def __validate_option_input(self, max_range: int):
        while True:
            opcao = input('=> Escolha uma opção: ')
            if opcao == '':
                self.__despedida()
                break
            elif not opcao.isdigit() or int(opcao) not in range(1,max_range+1):
                print('Não entendemos sua opção...')
                continue
            else:
                print(f'Opção {opcao} escolhida com sucesso!')
                return int(opcao)

    def __validate_str_input(self, title: str, mensagem: str):
        while True:
            string = input(mensagem)
            if string.replace('.','').isdigit() or len(string) < 3:
                print('Não entendemos sua escolha...')
                continue
            else:
                print(f'{title} cadastrado(a) com sucesso!')
                return string

    def __validate_number_input(self, title: str, mensagem: str, type: str):
        while True:
            number = input(mensagem)
            if not number.replace('.','').isdigit():
                print('Seu número está inválido')
                continue
            else:
                if type == 'int': return int(number)
                elif type == 'float': return float(number)

    def __escolher_acao(self):
        self.__print_menu('UMA AÇÃO', self.__acoes)
        self.__acao = self.__validate_option_input(len(self.__acoes))
    
    def __create_transporte(self):
        nome = self.__validate_str_input('Nome', 'Nome do transporte: ')
        altura = self.__validate_number_input('Altura', 'Altura do transporte: [m]', 'float')
        comprimento = self.__validate_number_input('Comprimento', 'Comprimento do transporte: [m]','float')
        carga = self.__validate_number_input('Carga', 'Carga do transporte: [ton]','float')
        velocidade = self.__validate_number_input('Velocidade', 'Velocidade do transporte: [Km/h]','float')
        if self.__tipo_transporte == 1:
            motor = self.__validate_str_input('Motor', 'Motor do transporte: ')
            rodas = self.__validate_str_input('Rodas', 'Rodas do transporte: ')
            return TransporteTerrestre(nome, altura, comprimento, carga, velocidade, motor, rodas)
        elif self.__tipo_transporte == 2:
            boca = self.__validate_number_input('Boca', 'Boca do transporte: [m]', 'float')
            calado = self.__validate_number_input('Calado', 'Calado do transporte: [m]', 'float')
            return TransporteAquatico(nome, altura, comprimento, carga, velocidade, boca, calado)
        elif self.__tipo_transporte == 3:
            autonomia = self.__validate_number_input('Autonomia', 'Autonomia do transporte: [Km]', 'float')
            envergadura = self.__validate_number_input('Envergadura', 'Envergadura do transporte: [m]', 'float')
            return TransporteAereo(nome, altura, comprimento, carga, velocidade, autonomia, envergadura)
          
    def __escolher_tipo_transporte(self):
        self.__print_menu('UM TIPO DE TRANSPORTE', self.__tipos_transportes)
        self.__tipo_transporte = self.__validate_option_input(len(self.__tipos_transportes))
        
    def cadastrar_transporte(self):
        print(f'--- CADASTRO DE {self.__tipos_transportes[self.__tipo_transporte][0].upper()}---')
        novo_transporte = self.__create_transporte()
        self.__transportes.append(novo_transporte)
        print(f'{novo_transporte.nome} cadastrado com sucesso!')

    def escolher_modelo_transporte(self):
        while True:
            print(F'---- MODELOS DE {self.__tipos_transportes[self.__tipo_transporte][0].upper()} ----')
            modelos = [transporte for transporte in self.__transportes if isinstance(transporte, self.__tipos_transportes[self.__tipo_transporte][1])]
            for index, transporte in enumerate(modelos):
                print(f'[{index+1}] | {transporte.nome}')
            transporte = modelos[self.__validate_option_input(len(modelos))-1]
            print(f'|NOME: {transporte.nome}')
            print(f'|ALTURA: {transporte.altura}')
            print(f'|COMPRIMENTO: {transporte.comprimento}')
            print(f'|CARGA: {transporte.carga}')
            print(f'|VELOCIDADE: {transporte.velocidade}')
            if self.__tipo_transporte == 1:
                print(f'|MOTOR: {transporte.carga}')
                print(f'|RODAS: {transporte.velocidade}')
            elif self.__tipo_transporte == 2:
                print(f'|BOCA: {transporte.boca}')
                print(f'|CALADO: {transporte.calado}')
            elif self.__tipo_transporte == 3:
                print(f'|AUTONOMIA: {transporte.autonomia}')
                print(f'|ENVERGADURA: {transporte.envergadura}')
                

    def iniciar(self):
        #mostrar mensagem de boas-vindas
        self.__boas_vindas()
        #mostrar menu com os tipos de transporte
        while True:
            self.__escolher_acao()
            #selecionar o tipo de transporte
            if self.__acao:
                self.__escolher_tipo_transporte()
            #ir para menu específico de acordo com a acao e tipo_transporte escolhidos
            if self.__tipo_transporte:
                if self.__acao == 1:
                    self.cadastrar_transporte()
                elif self.__acao == 2:
                    self.escolher_modelo_transporte()
        #self.__mostrar_transporte()
        #mostrar menu com os modelos do tipo escolhido
        #escolher o modelo
        #mostrar os detalhes do modelo escolhido
