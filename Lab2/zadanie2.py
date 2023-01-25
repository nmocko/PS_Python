# -*-coding: utf-8-*-
import re


def wczytaj():
    try:
        napis = input()
        return napis
    except EOFError:
        exit(0)


def rozpoznaj(napis):

    liczba = r"[0-9]+"
    wyraz = r"[a-zA-ZżźćńółęąśŻŹĆĄŚĘŁÓŃ]+"

    i = 0
    n = len(napis)
    while i < n:
        m = re.match(liczba, napis[i:])
        if m:
            print("Liczba:", m.group())
            i += len(m.group())
            continue
        m = re.match(wyraz, napis[i:])
        if m:
            print("Wyraz:", m.group())
            i += len(m.group())
            continue
        i += 1
    # m = re.findall(wyraz, napis)


if __name__ == '__main__':

    while True:
        napis = wczytaj()
        rozpoznaj(napis)


