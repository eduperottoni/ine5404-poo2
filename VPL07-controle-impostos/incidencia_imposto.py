from enum import Enum


'''
Enum contendo tres tipos de incidencia de impostos:
PRODUCAO, SERVICOS, VENDAS e TODOS
'''


class IncidenciaImposto(Enum):
    PRODUCAO = 1
    SERVICOS = 2
    VENDAS = 3
    TODOS = 4
