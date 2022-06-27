import pickle
from empresa import Empresa


class EmpresaDAO:
    def __init__(self, datasource='empresa.pkl'):
        self.__datasource = datasource
        self.__object_cache = {}

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__object_cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__object_cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, empresa: Empresa):
        self.__object_cache[empresa.cnpj] = empresa
        self.__dump()

    def remove(self, empresa: Empresa):
        try:
            del self.__object_cache[empresa.cnpj]
            self.__dump()
        except KeyError:
            pass

    def get(self, cnpj: int):
        try:
            return self.__object_cache[cnpj]
        except KeyError:
            pass

    def get_all(self) -> list:
        return self.__object_cache.values()
