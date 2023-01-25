from datetime import datetime


class Library:

    lib = []
    bor = []
    logs = {}

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
        # Library.lib.pop(n)
        # Book.instances.pop()
        Book.i -= 1

        if reader.pesel in Library.logs:
            Library.logs[reader.pesel].append(copy_book)
        else:
            Library.logs[reader.pesel] = []
            Library.logs[reader.pesel].append(reader)
            Library.logs[reader.pesel].append(copy_book)

        return reader.imie + " " + reader.nazwisko + " borrowed book: " + book.tytul + " id: " + str(book.id)

    @staticmethod
    def returnn(reader, book):

        if book.pesel != reader.pesel:
            return reader.imie + " " + reader.nazwisko + " didn't borrowed book: " + book.tytul + " id: " + str(book.id)

        now = datetime.now()

        l = len(Library.logs[reader.pesel])
        for i in range(1, l):
            if Library.logs[reader.pesel][i].id == book.id:
                Library.logs[reader.pesel][i].zwrot = Date(now.year, now.month, now.day, now.hour, now.minute)

        day0 = Date(0, 0, 0, 0, 0)
        book.wyporzyczenie = day0
        book.zwrot = day0
        book.pesel = 0

        return reader.imie + " " + reader.nazwisko + " returned book: " + book.tytul + " id: " + str(book.id)

    def __str__(self):

        r = ''
        for read in Library.logs:
            r += "Imie: " + Library.logs[read][0].imie + " Nazwisko: " + Library.logs[read][0].nazwisko + '\n'
            r += 30 * '*' + '\n'
            l = len(Library.logs[read])
            for i in range(1, l):
                if Library.logs[read][i].zwrot.rok == 0:
                    r += "Wyporzyczenie\nID: " + \
                         str(Library.logs[read][i].id) + \
                         "\nTytuł: " + Library.logs[read][i].tytul \
                         + "\nAutorzy: " + Library.logs[read][i].autorzy + "\nData wyporzyczenia: "
                    r += str(Library.logs[read][i].wyporzyczenie)
                    r += 30 * '-' + '\n'
                else:
                    r += "Wyporzyczenie + Zwrot\nID:" + str(Library.logs[read][i].id) + "\nTytuł: " + Library.logs[read][i].tytul \
                         + "\nAutorzy " + Library.logs[read][i].autorzy + "\nData wyporzyczenia: "
                    r += str(Library.logs[read][i].wyporzyczenie)
                    r += "Data zwrotu: "
                    r += str(Library.logs[read][i].zwrot)
                    r += 30*'-' + '\n'
            r += '\n\n'
        return r


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
    instances = []

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

    def __str__(self):
        r = "ID: " + str(self.id) + '\n'
        r += "Autorzy: " + self.autorzy + '\n'
        r += 'Tytuł: ' + self.tytul

        return r

    def __repr__(self):
        r = ''
        j = 1
        for instance in Book.instances:
            j += 1
            r += str(instance)
            r += '\n'
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
        return Library.borrow(self, book)

    def __sub__(self, book):
        return Library.returnn(self, book)


if __name__ == '__main__':

    reader1 = Reader("Jan", "Kowalski", 12345)
    reader2 = Reader("Julia", "Laskowska", 12342225)

    book1 = Book("Jan Brzechwa", "Na straganie")
    book2 = Book("Ula", "Lemoniada")
    book3 = Book("Matejko", "Bidon")
    book4 = Book("Jak", "Koić sen")

    Book.instances.append(book1)
    Book.instances.append(book2)
    Book.instances.append(book3)
    Library.lib.append(book1)
    Library.lib.append(book2)
    Library.lib.append(book3)

    print(book1)
    print(repr(book1))
    print(reader1)
    print(repr(reader1))

    print(reader1 + book2)
    print(reader2 - book2)
    print(reader2 + book2)
    print(reader1 + book1)
    print(reader1 - book2)
    print(reader2 + book3)
    print(reader2 + book2)
    print(reader2 + book4)

    print()
    print(Library())


