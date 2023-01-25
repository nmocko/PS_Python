import unittest
from io import StringIO
from unittest.mock import patch
from zadanie4 import Library


class TestLibrary(unittest.TestCase):

    def test_parseFileInput(self):
        file = open("books.txt", "r")
        lines = file.readlines()
        k = len(lines)
        file.close()
        Library.parseFileLine(lines, k)
        dict = {'Ania z Zielonego Wzgorza': '10', 'Dzieci z Bulerbyn': '12', 'Jak powstał wszechswiat': '10',
                'Od protonu do atomu': '2', 'Matematyka I': '12', 'Ile?': '9', 'Kolory świata': '2',
                'Kolorki': '3', 'Cos': '1'}
        self.assertEqual(Library.lib, dict)

    def test_parseInputLine1(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Library.parseInputLine("Koala kkkk kkkk")
            self.assertEqual(fake_out.getvalue(), "Złe dane wejściowe\n")

    def test_parseInputLine2(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Library.parseInputLine("Koala kkkk")
            self.assertEqual(fake_out.getvalue(), "Złe dane wejściowe\n")

    def test_parseInputLine3(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Library.parseInputLine('Koala 123 "Cos"')
            self.assertEqual(fake_out.getvalue(), "Złe dane wejściowe\n")

    def test_parseInputLine4(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Library.parseInputLine('K() kkkk "lll"')
            self.assertEqual(fake_out.getvalue(), "Złe dane wejściowe\n")

    def test_borrow1(self):
        Library.lib = {'Ania z Zielonego Wzgorza': '10', 'Dzieci z Bulerbyn': '12',
                       'Jak powstał wszechswiat': '10', 'Od protonu do atomu': '2', 'Matematyka I': '12',
                       'Ile?': '9', 'Kolory świata': '2', 'Kolorki': '3', 'Cos': '1'}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Library.borrow("Kowalki", "Mateamtyka od podstaw")
            self.assertEqual(fake_out.getvalue(), "We don't have this book\n")

    def test_borrow2(self):
        Library.lib = {'Ania z Zielonego Wzgorza': '0', 'Dzieci z Bulerbyn': '12', 'Jak powstał wszechswiat': '10',
                       'Od protonu do atomu': '2', 'Matematyka I': '12', 'Ile?': '9', 'Kolory świata': '2',
                       'Kolorki': '3', 'Cos': '1'}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Library.borrow("Kowalki", "Ania z Zielonego Wzgorza")
            self.assertEqual(fake_out.getvalue(), "We already borrowed this book\n")

    def test_borrow3(self):
        Library.lib = {'Ania z Zielonego Wzgorza': '1', 'Dzieci z Bulerbyn': '12', 'Jak powstał wszechswiat': '10',
                       'Od protonu do atomu': '2', 'Matematyka I': '12', 'Ile?': '9', 'Kolory świata': '2',
                       'Kolorki': '3', 'Cos': '1'}
        Library.bor = {'Kowalski': ['Ania z Zielonego Wzgorza', 'Dzieci z Bulerbyn'], 'Kowalska': ['Cos'],
                       'Kowal' : ['Kolorki']}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Library.borrow("Kowalki", "Ania z Zielonego Wzgorza")
            self.assertEqual(fake_out.getvalue(), "Kowalki borrowed book: Ania z Zielonego Wzgorza\n")

    def test_borrow4(self):
        Library.lib = {'Ania z Zielonego Wzgorza': '0', 'Dzieci z Bulerbyn': '12', 'Jak powstał wszechswiat': '10',
                       'Od protonu do atomu': '2', 'Matematyka I': '12', 'Ile?': '9', 'Kolory świata': '2',
                       'Kolorki': '3', 'Cos': '1'}
        Library.bor = {'Kowalski': ['Ania z Zielonego Wzgorza', 'Dzieci z Bulerbyn'], 'Kowalska': ['Cos'],
                       'Kowal' : ['Kolorki']}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Library.borrow("Grzybek", "Kolorki")
            self.assertEqual(fake_out.getvalue(), "Grzybek borrowed book: Kolorki\n")

    def test_return1(self):
        Library.lib = {'Ania z Zielonego Wzgorza': '0', 'Dzieci z Bulerbyn': '12', 'Jak powstał wszechswiat': '10',
                       'Od protonu do atomu': '2', 'Matematyka I': '12', 'Ile?': '9', 'Kolory świata': '2',
                       'Kolorki': '3', 'Cos': '1'}
        Library.bor = {'Kowalski': ['Ania z Zielonego Wzgorza', 'Dzieci z Bulerbyn'], 'Kowalska': ['Cos'],
                       'Kowal': ['Kolorki']}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Library.returnn("Kowal", "Kolorki")
            self.assertEqual(fake_out.getvalue(), "Kowal returned book: Kolorki\n")

    def test_return2(self):
        Library.bor = {'Kowalski': ['Ania z Zielonego Wzgorza', 'Dzieci z Bulerbyn'], 'Kowalska': ['Cos'],
                       'Kowal': ['Kolorki']}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Library.returnn("Wilk", "Kolorki")
            self.assertEqual(fake_out.getvalue(), "You didn't borrowed book\n")

    def test_return3(self):
        Library.lib = {'Ania z Zielonego Wzgorza': '0', 'Dzieci z Bulerbyn': '12', 'Jak powstał wszechswiat': '10',
                       'Od protonu do atomu': '2', 'Matematyka I': '12', 'Ile?': '9', 'Kolory świata': '2',
                       'Kolorki': '3', 'Cos': '1'}
        Library.bor = {'Kowalski': ['Ania z Zielonego Wzgorza', 'Dzieci z Bulerbyn'], 'Kowalska': ['Cos'],
                       'Kowal': ['Kolorki']}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Library.returnn("Kowal", "Matematyka I")
            self.assertEqual(fake_out.getvalue(), "You didn't borrowed this book\n")

    def full_test(self):

        file = open("books.txt", "r")
        lines = file.readlines()
        k = len(lines)
        file.close()
        Library.parseFileLine(lines, k)

        Library.parseInputLine('Mocko borrow "Matematyka I"')
        Library.parseInputLine('Mocko borrow "Ile?"')
        Library.parseInputLine('Kowalski borrow "Kolorki"')
        Library.parseInputLine('Kowalski borrow "Dzieci z Bulerbyn"')
        Library.parseInputLine('Mocko return "Matematyka I"')

        result = """-------------------------------------
----------      Books      ----------
Ania z Zielonego Wzgorza 10
Dzieci z Bulerbyn 11
Jak powstał wszechswiat 10
Od protonu do atomu 2
Matematyka I 12
Ile? 8
Kolory świata 2
Kolorki 2
Cos 1
----------     Readers     ----------
Mocko ['Ile?']
Kowalski ['Kolorki', 'Dzieci z Bulerbyn']
-------------------------------------
        """

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print("-" * 37)
            print("-" * 10, "     Books     ", "-" * 10)
            for i, j in Library.lib.items():
                print(i, j)
            print("-" * 10, "    Readers    ", "-" * 10)
            for i, j in Library.bor.items():
                print(i, j)
            print("-" * 37)
            self.assertEqual(fake_out.getvalue(), result)






if __name__ == '__main__':
    unittest.main()
