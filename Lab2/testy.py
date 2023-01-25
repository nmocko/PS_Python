import unittest
from io import StringIO
from unittest.mock import patch
from zadanie2 import rozpoznaj


class TestURLPrint(unittest.TestCase):

    def test_rozpoznaj_wyraz_liczba_wyraz(self):
        expected_out1 = 'Liczba: 90\nWyraz: koala\nLiczba: 90\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rozpoznaj("90koala90")
            self.assertEqual(fake_out.getvalue(), expected_out1)

    def test_rozpoznaj_wyraz(self):
        expected_out2 = 'Wyraz: Ala\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rozpoznaj("Ala")
            self.assertEqual(fake_out.getvalue(), expected_out2)

    def test_rozpoznaj_liczba(self):
        expected_out3 = 'Liczba: 901\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rozpoznaj("901")
            self.assertEqual(fake_out.getvalue(), expected_out3)

    def test_rozpoznaj_liczba_wyraz(self):
        expected_out3 = 'Liczba: 90\nWyraz: Ala\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rozpoznaj("90Ala")
            self.assertEqual(fake_out.getvalue(), expected_out3)

    def test_rozpoznaj_brak(self):
        expected_out4 = ""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rozpoznaj("____++++%%%")
            self.assertEqual(fake_out.getvalue(), expected_out4)

    def test_rozpoznaj_wyraz_brak_liczba(self):
        expected_out5 = 'Wyraz: Ala\nLiczba: 1\nLiczba: 13\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rozpoznaj("Ala_=1;;;13_")
            self.assertEqual(fake_out.getvalue(), expected_out5)

    def test_rozpoznaj_wyraz_literypolskie(self):
        expected_out6 = 'Wyraz: Łąka\nWyraz: Łańcuch\nLiczba: 15\nWyraz: Bazgrać\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rozpoznaj("Łąka {Łańcuch   15Bazgrać")
            self.assertEqual(fake_out.getvalue(), expected_out6)

    def test_rozpoznaj_wyraz_pl(self):
        expected_out7 = 'Wyraz: Alę\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rozpoznaj("Alę")
            self.assertEqual(fake_out.getvalue(), expected_out7)


if __name__ == '__main__':
    unittest.main()
