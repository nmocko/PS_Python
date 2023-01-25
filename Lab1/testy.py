#import sys
import unittest
#sys.path.append("/home/reny/PycharmProjects/programowanie_sktyptowe/Lab1/testy.py")
from zadanie1 import suma
from zadanie1 import MyException


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(suma(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(suma(2, 1.5), 3.5)

    def test_sum_integer_string(self):
       self.assertEqual(suma(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(suma('2.1', '2.0'), 4.1)

    def test_sum_rational_number(self):
        self.assertEqual(suma(1/2, 3/4), 5/4)

    def test_sum_complex_number(self):
        self.assertEqual(suma(4+5j, 1+3j), 5+8j)

    def test_sum_complex_float_number(self):
        self.assertEqual(suma(4.4+5j, 1-3j), 5.4+2j)

    # def test_sum_integer_wrong_number_in_string(self):
    #     self.assertEqual(suma(2, 'Ala ma kota123'), 2)

    def test_assert(self):
        self.assertRaises(MyException, suma, 'Ala ma kota123', 2)

    def test_different_forms(self):
        self.assertRaises(MyException, suma, 1, [2, 3])


if __name__ == '__main__':
    unittest.main()