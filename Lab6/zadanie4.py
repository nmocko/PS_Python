import argparse
import re
import warnings
import logging
from datetime import datetime
import sys


name = ""


def time_this(n, original_function):
    def new_function(*args,**kwargs):
        if original_function.__name__ != 'inner':
            logging.basicConfig(filename="Library.log", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
            msg = f'Użytkownik {name} wywołał metodę {original_function.__name__} klasy {n.__name__}'
            logging.warning(msg)
        x = original_function(*args, **kwargs)
        return x
    return new_function


def user(Cls):
    class NewCls(object):
        def __init__(self,*args,**kwargs):
            self.oInstance = Cls(*args,**kwargs)
        def __getattribute__(self,s):
            try:
                x = super(NewCls,self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__):
                return time_this(Cls, x)
            else:
                return x
    return NewCls



@user
class Library(object):

    def __init__(self):
        self.lib = {}
        self.bor = {}

    @staticmethod
    def admin(funkcja):
        def inner(*args, **kwargs):

            m = re.search(r' (.*)\.', str(funkcja))
            logging.basicConfig(filename="Library.log", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
            msg = f'Użytkownik {name} wywołał metodę {funkcja.__name__} klasy {m.group(1)}'
            logging.warning(msg)
            if name == 'ADMIN':
                return funkcja(*args, **kwargs)
            else:
                warnings.warn('You are not admin')
        return inner

    def borrow(self, fname, book):

        def fun(s):
            print(s)
            return True

        (book not in self.lib and fun("We don't have this book")) or \
            (int(self.lib[book]) == 0 and fun("We already borrowed this book")) or \
            (fname in self.bor and not self.bor[fname].append(book) and not self.lib.update({book: int(self.lib[book]) - 1})
                                                  and fun(f"{fname} borrowed book: {book}")) or \
            (int(self.lib[book]) != 0 and not self.lib.update({book: int(self.lib[book]) - 1}) and
                not self.bor.update({fname: [book]}) and fun(f"{fname} borrowed book: {book}"))


    def returnn(self, fname, book):

        def fun(s):
            print(s)
            return True

        (fname not in self.bor and fun("You didn't borrowed book")) or (book in self.bor[fname]
            and not self.bor[fname].remove(book)
            and not self.lib.update({book: int(self.lib[book]) + 1}) and fun(f"{fname} returned book: {book}")
        ) or (fun("You didn't borrowed this book"))


    def parseInputLine(self, line):
        wyr = r'([A-Za-z]+) ([A-Za-z]+) "(.*)"'
        m = re.search(wyr, line)
        if m == None:
            print("Złe dane wejściowe")
            return
        if m.group(2) == 'borrow':
            return 'borrow', m.group(1), m.group(3)
        elif m.group(2) == 'return':
            return 'return', m.group(1), m.group(3)
        else:
            print("No such option")
        return 1

    def parseFileLine(self, lines, k):
        wyr = r'^(.*?) ([0-9]+)\n'
        for i in range(k):
            m = re.search(wyr, lines[i])
            self.lib[m.group(1)] = m.group(2)
        return 1

    @admin
    def echo(self):
        r = ''
        r += "-" * 37 + '\n'
        r += "-" * 11 + "     Books     " + "-" * 11 + '\n'
        for i, j in self.lib.items():
            r += str(i) + ' ' + str(j) + '\n'
        r += "-" * 11 + "    Readers    " + "-" * 11 + '\n'
        for i, j in self.bor.items():
            r += str(i) + ' ' + str(j) + '\n'
        r += "-" * 37 + '\n'
        return r


if __name__ == '__main__':

    lib = Library()
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-f', metavar='FILE', type=argparse.FileType('r+'), nargs=1, help='Files to change')
    my_parser.add_argument('-name', metavar='login', type=str, nargs=1, help='Login')
    args = my_parser.parse_args()


    file = args.f[0]
    lines = file.readlines()
    k = len(lines)

    name = args.name[0]

    lib.parseFileLine(lines, k)
    print('FamilyName borrow/return "NameofBook"(in quatation)')
    lis = []

    while True:
        try:
            line = input()
            function, a, b = lib.parseInputLine(line)
            if function == 'borrow':
                lib.borrow(a, b)
            elif function == 'return':
                lib.returnn(a, b)

        except EOFError:
            break

    print(lib.echo())
