import sys

slownik = {}


def zapisz(tab):
    n = len(tab)
    for i in range(1, n):
        if tab[i] in slownik:
            slownik[tab[i]] = int(slownik[tab[i]]) + 1
        else:
            slownik[tab[i]] = 1
    # print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))


def wypisz():
    n = len(slownik)
    for v, w in slownik.items():
        if n == 1:
            print(v, ':', w)
            break
        print(v, ':', w, end=', ')
        n -= 1


if __name__ == '__main__':
    # print('Ładowanie modułu "{0}"'.format(__name__))
    # print('Załadowano moduł "{0}"'.format(__name__))
    n = len(sys.argv)
    if n != 0:
        zapisz(sys.argv)
    wypisz()
