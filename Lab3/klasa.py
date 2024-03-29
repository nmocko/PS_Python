import sys
##################################
def methodBody(self, name):
    return "Wywołano metodę \033[{color}m{name:^17}\033[0m obiektu \033[{color}m{objectId}\033[0m".format(
            name     = name,
            color    = "38:5:{}".format(id(self) % 13 + 1),
            objectId = id(self)
        )
##################################
class Klasa(object):
    tab = [1, 2, 3]
    def __init__(self, tab, a, b):
        self.tab = tab
        self._zmienna1 = a
        self.__zmienna2 = b
        # print(obiekt._Klasa__zmienna2)
        print(methodBody(self, sys._getframe().f_code.co_name))

    def __del__(self):
        print(methodBody(self, sys._getframe().f_code.co_name))

    def __str__(self):
        return methodBody(self, sys._getframe().f_code.co_name)

    def __repr__(self):
        return methodBody(self, sys._getframe().f_code.co_name)

    def metodaInstancyjna(self):
        # global tab
        print('Zmienna tab instancyjna: ', self.tab)
        print('Zmienna tab klasowa: ', Klasa.tab)
        print(methodBody(self, sys._getframe().f_code.co_name))

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę \033[1m{name:^17}\033[0m klasy   \033[1m{cls}\033[0m".format(
            name = sys._getframe().f_code.co_name,
            cls  = cls.__name__)
        )

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę \033[1m{name:^17}\033[0m klasy   \033[1m{cls}\033[0m".format(
            name = sys._getframe().f_code.co_name,
            cls  = __class__.__name__)
        )
##################################
print("Załadowano zawartość pliku '{name}'".format(name=__file__))