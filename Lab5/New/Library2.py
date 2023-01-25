from abc import ABC, abstractmethod
from datetime import datetime


class Library:

    lib = []
    bor = []
    logswyp = {}
    logskup = {}
    skl = []
    suma = 0
    buyer = {}

    @staticmethod
    def borrow(reader, book):
        n = len(Library.lib)
        m = len(Library.bor)
        f = 0
        j = -1
        for i in range(n):
            if book.id == Library.lib[i].id:
                f = 1
                j = i
        if f == 0:
            return "We don't have this book: " + book.tytul

        if Library.lib[j].pesel != 0:
            return "The book: " + book.tytul + " has been already borrowed"

        f = 0
        for i in range(m):
            if reader.pesel == Library.bor[i].pesel:
                f = 1
        if f == 0:
            return reader.imie + " " + reader.nazwisko + " is not in our Library"

        now = datetime.now()
        book.wyporzyczenie = Date(now.year, now.month, now.day, now.hour, now.minute)
        book.pesel = reader.pesel
        copy_book = Book(book.autorzy, book.tytul, book.id, book.pesel)
        copy_book.wyporzyczenie = Date(now.year, now.month, now.day, now.hour, now.minute)
        Book.i -= 1

        if reader.pesel in Library.logswyp:
            Library.logswyp[reader.pesel].append(copy_book)
        else:
            Library.logswyp[reader.pesel] = []
            Library.logswyp[reader.pesel].append(reader)
            Library.logswyp[reader.pesel].append(copy_book)

        return reader.imie + " " + reader.nazwisko + " borrowed book: " + book.tytul + " id: " + str(book.id)

    @staticmethod
    def returnn(reader, book):

        if book.pesel != reader.pesel:
            return reader.imie + " " + reader.nazwisko + " didn't borrowed book: " + book.tytul + " id: " + str(book.id)

        now = datetime.now()

        l = len(Library.logswyp[reader.pesel])
        for i in range(1, l):
            if Library.logswyp[reader.pesel][i].id == book.id:
                Library.logswyp[reader.pesel][i].zwrot = Date(now.year, now.month, now.day, now.hour, now.minute)

        day0 = Date(0, 0, 0, 0, 0)
        book.wyporzyczenie = day0
        book.zwrot = day0
        book.pesel = 0

        return reader.imie + " " + reader.nazwisko + " returned book: " + book.tytul + " id: " + str(book.id)

    @staticmethod
    def buy(reader, book):

        if book.ilosc < 1:
            return "We have already sold this books"

        Library.suma += book.cena
        book.ilosc -= 1

        if reader.pesel in Library.buyer:
            l = len(Library.buyer[reader.pesel])
            f = 0
            for i in range(l):
                if book.id == Library.buyer[reader.pesel][i][0].id:
                    Library.buyer[reader.pesel][i][1] += 1
                    f = 1
            if f == 0:
                Library.buyer[reader.pesel].append([book, 1])

        else:
            Library.buyer[reader.pesel] = []
            Library.buyer[reader.pesel].append([book, 1])

        if book.id in Library.logskup:
            Library.logskup[book.id].append(reader)
        else:
            Library.logskup[book.id] = []
            Library.logskup[book.id].append(reader)

        return reader.imie + " " + reader.nazwisko + " bought " + book.tytul + " price " + str(book.cena)

    @staticmethod
    def echo(visitor):

        if isinstance(visitor, Reader):
            r = ''
            for read in Library.logswyp:
                if Library.logswyp[read][0].pesel == visitor.pesel:
                    r += "Imie: " + Library.logswyp[read][0].imie + " Nazwisko: " + Library.logswyp[read][0].nazwisko + '\n'
                    r += 30 * '*' + '\n'
                    l = len(Library.logswyp[read])
                    for i in range(1, l):
                        if Library.logswyp[read][i].zwrot.rok == 0:
                            r += "Wyporzyczenie\nID: " + \
                                 str(Library.logswyp[read][i].id) + \
                                 "\nTytuł: " + Library.logswyp[read][i].tytul \
                                 + "\nAutorzy: " + Library.logswyp[read][i].autorzy + "\nData wyporzyczenia: "
                            r += str(Library.logswyp[read][i].wyporzyczenie)
                            r += 30 * '-' + '\n'
                        else:
                            r += "Wyporzyczenie + Zwrot\nID:" + str(Library.logswyp[read][i].id) + "\nTytuł: " + \
                                 Library.logswyp[read][i].tytul \
                                 + "\nAutorzy " + Library.logswyp[read][i].autorzy + "\nData wyporzyczenia: "
                            r += str(Library.logswyp[read][i].wyporzyczenie)
                            r += "Data zwrotu: "
                            r += str(Library.logswyp[read][i].zwrot)
                            r += 30 * '-' + '\n'
                    r += '\n'
                    return r
            return "Imie: " + visitor.imie + " Nazwisko: " + visitor.nazwisko + "is not reader in our Library"

        elif isinstance(visitor, Buyer):
            r = ''
            koszt = 0
            r += "ZAKUP:\n"
            r += visitor.imie + ' ' + visitor.nazwisko + '\n'
            if visitor.pesel in Library.buyer:
                l = len(Library.buyer[visitor.pesel])
                for i in range(l):
                    short = Library.buyer[visitor.pesel][i][0]
                    r += f'- {short.tytul} {short.autorzy} cena {short.cena} PLN ilosc {Library.buyer[visitor.pesel][i][1]} sztuk\n'
                    koszt += short.cena * Library.buyer[visitor.pesel][i][1]
                r += f'KOSZT = {koszt} PLN\n'
                return r
            return "Imie: " + visitor.imie + " Nazwisko: " + visitor.nazwisko + "is not buyer in our Library"


class Date:

    def __init__(self, rok, miesiac, dzien, godzina, minuta):
        self.rok = rok
        self.miesiac = miesiac
        self.dzien = dzien
        self.godzina = godzina
        self.minuta = minuta

    def __str__(self):
        r = str(self.dzien) + '.'
        if self.miesiac < 10:
            r += '0' + str(self.miesiac) + '.'
        else:
            r += str(self.miesiac) + '.'
        r += str(self.rok) + ' '
        if self.minuta > 9:
            r += str(self.godzina) + ':'
            r += str(self.minuta) + '\n'
        else:
            r += str(self.godzina) + ':0'
            r += str(self.minuta) + '\n'
        return r


class Book:

    i = 1

    def __init__(self, autorzy, tytul, id = -1, pesel=0, rok1=0, miesiac1=0, dzien1=0, godzina1=0, minuta1=0, rok2=0,
                 miesiac2=0, dzien2=0, godzina2=0, minuta2=0):
        if id != -1:
            self.id = id
        else:
            self.id = Book.i
            Book.i += 1
        self.pesel = pesel
        self.autorzy = autorzy
        self.tytul = tytul
        self.wyporzyczenie = Date(rok1, miesiac1, dzien1, godzina1, minuta1)
        self.zwrot = Date(rok2, miesiac2, dzien2, godzina2, minuta2)
        # Library.lib.append(self)
        # Book.instances.append(self)

    def __repr__(self):
        r = "ID: " + str(self.id) + '\n'
        r += "Autorzy: " + self.autorzy + '\n'
        r += 'Tytuł: ' + self.tytul

        return r


class BorrowBook(Book):

    instances = []

    def __init__(self, autorzy, tytul, id = -1, pesel=0, rok1=0, miesiac1=0, dzien1=0, godzina1=0, minuta1=0, rok2=0,
                 miesiac2=0, dzien2=0, godzina2=0, minuta2=0):
        self.pesel = pesel
        super().__init__(autorzy, tytul, id)
        self.wyporzyczenie = Date(rok1, miesiac1, dzien1, godzina1, minuta1)
        self.zwrot = Date(rok2, miesiac2, dzien2, godzina2, minuta2)
        # Library.lib.append(self)
        # Book.instances.append(self)

    def __str__(self):

        r = ''
        for read in Library.logswyp:
            r += "Imie: " + Library.logswyp[read][0].imie + " Nazwisko: " + Library.logswyp[read][0].nazwisko + '\n'
            r += 30 * '*' + '\n'
            l = len(Library.logswyp[read])
            for i in range(1, l):
                if Library.logswyp[read][i].zwrot.rok == 0:
                    r += "Wyporzyczenie\nID: " + \
                         str(Library.logswyp[read][i].id) + \
                         "\nTytuł: " + Library.logswyp[read][i].tytul \
                         + "\nAutorzy: " + Library.logswyp[read][i].autorzy + "\nData wyporzyczenia: "
                    r += str(Library.logswyp[read][i].wyporzyczenie)
                    r += 30 * '-' + '\n'
                else:
                    r += "Wyporzyczenie + Zwrot\nID:" + str(Library.logswyp[read][i].id) + "\nTytuł: " + Library.logswyp[read][i].tytul \
                         + "\nAutorzy " + Library.logswyp[read][i].autorzy + "\nData wyporzyczenia: "
                    r += str(Library.logswyp[read][i].wyporzyczenie)
                    r += "Data zwrotu: "
                    r += str(Library.logswyp[read][i].zwrot)
                    r += 30*'-' + '\n'
            r += '\n\n'
        return r


class BuyBook(Book):

    instances = []

    def __init__(self, autorzy, tytul, cena, ilosc, id = -1, pesel=0, rok1=0, miesiac1=0, dzien1=0, godzina1=0, minuta1=0, rok2=0,
                 miesiac2=0, dzien2=0, godzina2=0, minuta2=0):
        self.pesel = pesel
        self.cena = cena
        self.ilosc = ilosc
        super().__init__(autorzy, tytul, id)
        self.wyporzyczenie = Date(rok1, miesiac1, dzien1, godzina1, minuta1)
        self.zwrot = Date(rok2, miesiac2, dzien2, godzina2, minuta2)
        Library.skl.append(self)
        # Library.lib.append(self)
        # Book.instances.append(self)

    def __str__(self):
        r = ''
        z = len(Library.skl)
        for el in Library.logskup:
            for j in range(z):
                if el == Library.skl[j].id:
                    r += Library.skl[j].tytul + ' ' + Library.skl[j].autorzy + ' sprzedana ilosc ' + str(len(Library.logskup[el])) + '\n'
        r += 'SUMA = ' + str(Library.suma)
        return r


class Visitor(ABC):

    def __init__(self, imie, nazwisko, pesel):
        self.nazwisko = nazwisko
        self.imie = imie
        self.pesel = pesel

    def __lshift__(self, book):
        if isinstance(self, Reader):
            return "You can only borrow and return books"
        if isinstance(book, BuyBook):
            return Library.buy(self, book)
        else:
            return "You can only borrow this book"

    def __add__(self, book):
        if isinstance(self, Buyer):
            return "You can only buy books"
        if isinstance(book, BorrowBook):
            return Library.borrow(self, book)
        else:
            print("You can only buy this book")

    def __sub__(self, book):
        if isinstance(self, Buyer):
            return "You can onlu buy books"
        if isinstance(book, BorrowBook):
            return Library.returnn(self, book)
        else:
            print("You can only buy this book")


class Buyer(Visitor):

    def __init__(self, imie, nazwisko, pesel):
        super().__init__(imie, nazwisko, pesel)
        Library.bor.append(self)
        Reader.instances.append(self)


class Reader(Visitor):

    instances = []

    def __init__(self, imie, nazwisko, pesel):
        super().__init__(imie, nazwisko, pesel)
        Library.bor.append(self)
        Reader.instances.append(self)

    def __str__(self):
        r = "Imie: " + self.imie + '\n'
        r += "Nazwisko: " + self.nazwisko + '\n'
        return r

    def __repr__(self):
        r = ''
        j = 1
        for instance in Reader.instances:
            r += str(j) + '.    '
            j += 1
            r += str(instance)
        return r



if __name__ == '__main__':

    reader1 = Reader("Jan", "Kowalski", 12345)
    reader2 = Reader("Julia", "Laskowska", 12342225)

    buyer1 = Buyer("Martyna", "Nosek", 1209)
    buyer2 = Buyer("Jan", "Słowik", 1219)

    book1 = BorrowBook("Jan Brzechwa", "Na straganie")
    book2 = BorrowBook("Ula", "Lemoniada")
    book3 = BorrowBook("Matejko", "Bidon")
    book4 = BorrowBook("Jak", "Koić sen")

    BorrowBook.instances.append(book1)
    BorrowBook.instances.append(book2)
    BorrowBook.instances.append(book3)
    Library.lib.append(book1)
    Library.lib.append(book2)
    Library.lib.append(book3)

    print(reader1)

    print(reader1 + book2)
    print(reader2 - book2)
    print(reader2 + book2)
    print(reader1 + book1)
    print(reader1 - book2)
    print(reader2 + book3)
    print(reader2 + book2)
    print(reader2 + book4)

    book5 = BuyBook("Adam Mickiewicz", "Pan Tadeusz", 10, 2)
    book6 = BuyBook("William Sheakspear", "Romeo i Julia", 15, 1)
    book7 = BuyBook("Adam Mickiewicz", "Dziady", 21, 5)
    book8 = BuyBook("Adam Mickiewicz", "Ballady i romanse", 21, 5)
    print(buyer1 << book5)
    print(buyer1 << book5)
    print(buyer1 << book5)
    print(reader2 << book2)
    print(buyer1 << book6)
    print(buyer2 << book7)

    print()
    print(Library.echo(reader1))
    print(Library.echo(buyer1))

    print(book1)
    print(book5)
