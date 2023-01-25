import argparse
import re


class Library:

    lib = {}
    bor = {}

    @staticmethod
    def borrow(fname, book):
        if book not in Library.lib:
            print("We don't have this book")
            return
        if int(Library.lib[book]) == 0:
            print("We already borrowed this book")
            return
        if fname in Library.bor:
            Library.bor[fname].append(book)
            Library.lib[book] = int(Library.lib[book]) - 1
            print(fname, "borrowed book:", book)
        else:
            Library.bor[fname] = []
            Library.bor[fname].append(book)
            Library.lib[book] = int(Library.lib[book]) - 1
            print(fname, "borrowed book:", book)

    @staticmethod
    def returnn(fname, book):
        if fname not in Library.bor:
            print("You didn't borrowed book")
            return
        l = len(Library.bor[fname])
        for i in range(l):
            if Library.bor[fname][i] == book:
                Library.bor[fname].remove(book)
                Library.lib[book] = int(Library.lib[book]) + 1
                print(fname, "returned book:", book)
                return
        print("You didn't borrowed this book")

    @staticmethod
    def parseInputLine(line):
        wyr = r'([A-Za-z]+) ([A-Za-z]+) "(.*)"'
        m = re.search(wyr, line)
        if m == None:
            print("Złe dane wejściowe")
            return
        if m.group(2) == 'borrow':
            Library.borrow(m.group(1), m.group(3))
        elif m.group(2) == 'return':
            Library.returnn(m.group(1), m.group(3))
        else:
            print("No such option")

    @staticmethod
    def parseFileLine(lines, k):
        wyr = r'^(.*?) ([0-9]+)\n'
        for i in range(k):
            m = re.search(wyr, lines[i])
            Library.lib[m.group(1)] = m.group(2)


if __name__ == '__main__':

    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('revs', metavar='FILE', type=argparse.FileType('r+'), nargs=1, help='Files to change')
    args = my_parser.parse_args()

    file = args.revs[0]
    lines = file.readlines()
    k = len(lines)

    Library.parseFileLine(lines, k)
    print('FamilyName borrow/return "NameofBook"(in quatation)')
    lis = []

    while True:
        try:
            line = input()
            Library.parseInputLine(line)

        except EOFError:
            break

    print("-"*37)
    print("-"*10, "     Books     ", "-"*10)
    for i, j in Library.lib.items():
        print(i, j)
    print("-" * 10, "    Readers    ", "-" * 10)
    for i, j in Library.bor.items():
        print(i, j)
    print("-"*37)

