import sys

lista = []


def zapisz(tab):
    n = len(tab)
    for i in range(1, n):
        m = len(lista)
        f = 0
        for j in range(m):
            if lista[j][0] == tab[i]:
                lista[j][1] += 1
                f = 1
        if f == 0:
            lista.append([tab[i], 1])


def wypisz():
    m = len(lista)
    for i in range(m-1):
        print(lista[i][0], ':', lista[i][1], end=', ')
    print(lista[m-1][0], ':', lista[m-1][1])
    # print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))


if __name__ == '__main__':
    # print('Ładowanie modułu "{0}"'.format(__name__))
    # print('Załadowano moduł "{0}"'.format(__name__))
    n = len(sys.argv)
    if n != 0:
        zapisz(sys.argv)
    wypisz()
