import slownik
import lista
import sys
import getopt


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'm:', ["moduł="])
    except getopt.GetoptError as err:
        print("Poprawna składnia: python3 ./zadanie3_2.py --moduł=(lista/slownik)")
        opts = []

    for opt, arg in opts:
        if opt in ['-m', '--moduł']:
            if arg == 'lista':
                lista.zapisz(sys.argv[1:])
                lista.wypisz()
            elif arg == 'slownik':
                slownik.zapisz(sys.argv[1:])
                slownik.wypisz()
            else:
                print('Poprawne opcje to --moduł=lista lub --moduł=slownik')
        else:
            print("Nie ma takiej opcji")
            assert False
