from abc import ABC, abstractmethod
from datetime import datetime


class Library:

    lib = []
    bor = []
    logswyp = {}
    logskup = {}
    skl = []
    suma = 0

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
        if book.id in Library.logskup:
            Library.logskup[book.id] += 1
        else:
            Library.logskup[book.id] = 1

        return reader.imie + " " + reader.nazwisko + " bought " + book.tytul + " price " + str(book.cena)


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


class Book(ABC):

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
                    r += Library.skl[j].tytul + ' ' + Library.skl[j].autorzy + ' sprzedana ilosc ' + str(Library.logskup[el]) + '\n'
        r += 'SUMA = ' + str(Library.suma)
        return r


class Reader:

    instances = []

    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
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

    def __add__(self, book):
        if isinstance(book, BorrowBook):
            return Library.borrow(self, book)
        else:
            print("You can only buy this book")

    def __sub__(self, book):
        if isinstance(book, BorrowBook):
            return Library.returnn(self, book)
        else:
            print("You can only buy this book")

    def __lshift__(self, book):
        if isinstance(book, BuyBook):
            return Library.buy(self, book)
        else:
            return "You can only borrow this book"


if __name__ == '__main__':

    reader1 = Reader("Jan", "Kowalski", 12345)
    reader2 = Reader("Julia", "Laskowska", 12342225)

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

    print(book1)
    print(reader1)

    print(reader1 + book2)
    print(reader2 - book2)
    print(reader2 + book2)
    print(reader1 + book1)
    print(reader1 - book2)
    print(reader2 + book3)
    print(reader2 + book2)
    print(reader2 + book4)

    print(book1)

    book5 = BuyBook("Adam Mickiewicz", "Pan Tadeusz", 10, 2)
    print(reader1 << book5)
    print(reader1 << book5)
    print(reader1 << book5)
    print(reader2 << book2)

    print(book5)



