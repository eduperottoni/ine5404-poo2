class ElevadorJahNoTerreoException(Exception):
    def __init__(self):
        super().__init__("O elevador ja esta no terreo")
