import unittest
from zadanie3 import Library, Book, Reader, Date
from datetime import datetime


class UnittestZadanie3(unittest.TestCase):

    book1 = Book("Adam Mickiewicz", "Pan Tadeusz")
    book2 = Book("Stanisław Lem", "Solaris")
    book3 = Book("Magdalena Witkiewicz, Stefan Darda", "Cymanowski Młyn")
    book4 = Book("Ryszard Kapuściński", "Heban")
    reader1 = Reader("Jan", "Kowalski", 12345)
    reader2 = Reader("Julia", "Laskowska", 122333)
    reader3 = Reader("Agnieszka", "Rydz", 11121314151617)
    Book.instances.append(book1)
    Book.instances.append(book2)
    Book.instances.append(book4)
    Library.lib.append(book1)
    Library.lib.append(book2)
    Library.lib.append(book4)

    def test_Book(self):

        self.assertEqual(str(UnittestZadanie3.book3), "ID: 3\nAutorzy: Magdalena Witkiewicz, Stefan Darda\nTytuł: Cymanowski Młyn")
        self.assertEqual(str(UnittestZadanie3.book2), "ID: 2\nAutorzy: Stanisław Lem\nTytuł: Solaris")
        self.assertEqual(str(UnittestZadanie3.book1), "ID: 1\nAutorzy: Adam Mickiewicz\nTytuł: Pan Tadeusz")

        self.assertEqual(repr(UnittestZadanie3.book1), "ID: 1\nAutorzy: Adam Mickiewicz\nTytuł: Pan Tadeusz\nID: 2\nAutorzy: Stanisław "
                                      "Lem\nTytuł: Solaris\nID: 4\nAutorzy: Ryszard Kapuściński\nTytuł: Heban\n")

    def test_Date(self):

        date1 = Date(2021, 12, 8, 7, 0)
        date2 = Date(2020, 7, 12, 12, 19)
        date3 = Date(9999, 9, 9, 9, 9)

        self.assertEqual(str(date1), "8.12.2021 7:00\n")
        self.assertEqual(str(date2), "12.07.2020 12:19\n")
        self.assertEqual(str(date3), "9.09.9999 9:09\n")

    def test_Reader(self):

        self.assertEqual(str(UnittestZadanie3.reader1), "Imie: Jan\nNazwisko: Kowalski\n")
        self.assertEqual(str(UnittestZadanie3.reader2), "Imie: Julia\nNazwisko: Laskowska\n")
        self.assertEqual(str(UnittestZadanie3.reader3), "Imie: Agnieszka\nNazwisko: Rydz\n")

        self.assertEqual(repr(UnittestZadanie3.reader1), "1.    Imie: Jan\nNazwisko: Kowalski\n2.    Imie: Julia\nNazwisko: Laskowska\n"
                                        "3.    Imie: Agnieszka\nNazwisko: Rydz\n")

    def test_add_subb(self):

        self.assertEqual(UnittestZadanie3.reader1 + UnittestZadanie3.book1, "Jan Kowalski borrowed book: Pan Tadeusz id: 1")
        self.assertEqual(UnittestZadanie3.reader2 + UnittestZadanie3.book2, "Julia Laskowska borrowed book: Solaris id: 2")

        self.assertEqual(UnittestZadanie3.reader1 - UnittestZadanie3.book1,
                         "Jan Kowalski returned book: Pan Tadeusz id: 1")
        self.assertEqual(UnittestZadanie3.reader2 - UnittestZadanie3.book2,
                         "Julia Laskowska returned book: Solaris id: 2")

    def test_complex(self):
        self.assertEqual(UnittestZadanie3.reader1 + UnittestZadanie3.book1,
                         "Jan Kowalski borrowed book: Pan Tadeusz id: 1")
        self.assertEqual(UnittestZadanie3.reader2 + UnittestZadanie3.book2,
                         "Julia Laskowska borrowed book: Solaris id: 2")
        self.assertEqual(UnittestZadanie3.reader1 + UnittestZadanie3.book2,
                         "The book: Solaris has been already borrowed")
        self.assertEqual(UnittestZadanie3.reader1 + UnittestZadanie3.book3,
                         "We don't have this book: Cymanowski Młyn")
        self.assertEqual(UnittestZadanie3.reader3 + UnittestZadanie3.book4,
                         "Agnieszka Rydz borrowed book: Heban id: 4")
        self.assertEqual(UnittestZadanie3.reader1 - UnittestZadanie3.book2,
                         "Jan Kowalski didn't borrowed book: Solaris id: 2")
        self.assertEqual(UnittestZadanie3.reader1 - UnittestZadanie3.book1,
                         "Jan Kowalski returned book: Pan Tadeusz id: 1")
        self.assertEqual(UnittestZadanie3.reader2 - UnittestZadanie3.book2,
                         "Julia Laskowska returned book: Solaris id: 2")

        now = datetime.now()
        date = Date(now.year, now.month, now.day, now.hour, now.minute)

        self.assertEqual(str(Library()), "Imie: Jan Nazwisko: Kowalski\n******************************\nWyporzyczenie "
                                           "+ Zwrot\nID:1\nTytuł: Pan Tadeusz\nAutorzy Adam Mickiewicz\nData "
                                           "wyporzyczenia: " + str(date) + "Data zwrotu: " + str(date) +
                                            "-------------"
                                           "-----------------\nWyporzyczenie + Zwrot\nID:1\nTytuł: Pan Tadeusz\nAutorzy "
                                           "Adam Mickiewicz\nData wyporzyczenia: " + str(date) + "Data zwrotu: "
                                            + str(date) +
                                           "------------------------------\n\n\nImie: Julia Nazwisko: Laskowska\n"
                                           "******************************\nWyporzyczenie + Zwrot\nID:2\nTytuł: Solaris\n"
                                           "Autorzy Stanisław Lem\nData wyporzyczenia: " + str(date) + "Data zwrotu: "
                                           + str(date) + "------------------------------\nWyporzyczenie + Zwrot\nID:2\n"
                                           "Tytuł: Solaris\nAutorzy Stanisław Lem\nData wyporzyczenia: "
                                           + str(date) + "Data zwrotu: " + str(date) + "------------------------------\n"
                                           "\n\nImie: Agnieszka Nazwisko: Rydz\n******************************\nWyporzyczenie\n"
                                           "ID: 4\nTytuł: Heban\nAutorzy: Ryszard Kapuściński\nData wyporzyczenia: "
                                           + str(date) + "------------------------------\n\n\n")


if __name__ == '__main__':
    unittest.main()
