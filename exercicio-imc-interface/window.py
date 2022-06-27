import PySimpleGUI as sg

class Window:
    def __init__(self, titulo: str):
        self.__titulo = titulo
        self.__lista_linhas = [
            [sg.Text('Seu peso: '), sg.InputText('', key='peso'), sg.Text('Kg')],
            [sg.Text('Sua altura: '), sg.InputText('', key='altura'), sg.Text('m')],
            [sg.Text('Seu IMC é'), sg.Text('',key='imc', size=(6,1))],
            [sg.Text('', key='classificacao-validacao')],
            [sg.Text('', size=(14,1)), sg.Button('Calcular IMC')] 
        ]
        
    def gerar_tela(self):
        return sg.Window(self.__titulo, self.__lista_linhas)
