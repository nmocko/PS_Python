class Operacje:

    argumentySuma = [4, 5]
    argumentyRoznica = [4, 5, 6]

    def argumenty(*args, **kwarg):
        def decorator(function):
            def inner(*arg, **kwargs):
                tul = arg
                z = getattr(Operacje, args[0])
                for i in z:
                    tul = (*tul, i)
                if not function(*tul, **kwargs):
                    if function.__qualname__ == 'Operacje.suma':
                        if len(tul) > 3:
                            return tul[3]
                    elif function.__qualname__ == 'Operacje.roznica':
                        if len(tul) > 2:
                            return tul[2]
                    else:
                        return None
                else:
                    return function(*tul, **kwargs)
            return inner
        return decorator

    def __init__(self):
        self.record = {"roznica": None, "suma": None}

    def __setitem__(self, key, newlist):
        if key == "roznica":
            Operacje.argumentyRoznica = newlist
        elif key == "suma":
            Operacje.argumentySuma = newlist

    @staticmethod
    @argumenty('argumentySuma')
    def suma(a, b, c, *kwargs):
        print("%d+%d+%d=%d" % (a, b, c, a+b+c))

    @staticmethod
    @argumenty('argumentyRoznica')
    def roznica(x, y, *kwargs):
        print("%d-%d=%d" % (x, y, x-y))


if __name__ == '__main__':
    op=Operacje()
    op.suma(1, 2, 3) #Wypisze: 1+2+3=6
    op.suma(1,2) #Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
    op.suma(1) #Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
    #op.suma() #TypeError: suma() takes exactly 3 arguments (2 given)
    op.roznica(2,1) #Wypisze: 2-1=1
    op.roznica(2) #Wypisze: 2-4=-2
    wynik=op.roznica() #Wypisze: 4-5=-1
    print(wynik) #Wypisze: 6

    #Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
    op['suma'] = [1, 2]
    #oznacza, że   argumentySuma=[1,2]

    #Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
    op['roznica'] = [1, 2, 3]
    #oznacza, że   argumentyRoznica=[1,2,3]
    op.suma(1,2)
    op.roznica(2)
    x = op.suma(7, 9)
    print(x)
