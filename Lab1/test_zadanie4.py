import unittest
from zadanie4 import dane
from zadanie4 import sklep
from zadanie4 import towar
from zadanie4 import historia


class Test_TestSklep(unittest.TestCase):

    def test_dane1(self):
        self.assertEqual(sklep("Kupno","mango", 80, "Koszyk"), "OK, kupiles")
    def test_dane2(self):
        self.assertEqual(sklep("Kupno","mango", 120, "Wakra"), "Za mało produktów na stanie")
    def test_dane3(self):
        self.assertEqual(sklep("Kupno","winogrono", 80, "Koszyk"), "Nie ma takiego produktu")
    def test_dane4(self):
        self.assertEqual(sklep("Oddanie","mango", 80, "Koszyk"), "Nie ma takiej komendy")
    def test_dane5(self):
        self.assertEqual(sklep("Sprzedarz","mango", 80, "Koszyk"), "Sprzedane")
    print(historia)