import slownik
import lista
import sys


if __name__ == '__main__':
    if sys.argv[1] == '--lista':
        lista.zapisz(sys.argv[1:])
        lista.wypisz()
    elif sys.argv[1] == '--slownik':
        slownik.zapisz(sys.argv[1:])
        slownik.wypisz()
    else:
        print('Poprawna składnia: python3 ./zadanie3_1.py --lista/--slownik {argumenty (liczby)}')
