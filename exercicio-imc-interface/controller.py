from window import Window
from imc import Imc
import PySimpleGUI as sg

class Controller:
    def __init__(self, titulo: str):
        self.__titulo = titulo
    
    def iniciar(self):
        window = Window(self.__titulo).gerar_tela()
        rodando = True
        while rodando:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Calcular IMC':
                imc = Imc(values['peso'], values['altura'])
                if imc.validar_entradas():
                    classificacao = imc.classificar_imc()
                    window.Element('imc').Update(imc.calcular_imc())
                    window.Element('classificacao-validacao').Update(classificacao)
                else:
                    window.Element('classificacao-validacao').Update('Entrada inválida! Tente novamente')
                    window.Element('imc').Update('')
                    continue
        window.close()

        
        
