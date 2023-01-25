import unittest
from io import StringIO
from unittest.mock import patch
from dekorator import Operacje


class UnitTestOpercaje(unittest.TestCase):

    def test_dekorator(self):
        op = Operacje()
    # test suma basic
        with patch('sys.stdout', new=StringIO()) as fake_out:
            op.suma(1, 2, 3)
            r = '1+2+3=6\n'
            self.assertEqual(fake_out.getvalue(), r)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            op.suma(5, 6)
            r = '5+6+4=15\n'
            self.assertEqual(fake_out.getvalue(), r)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            op.suma(1)
            r = '1+4+5=10\n'
            self.assertEqual(fake_out.getvalue(), r)
    # test roznica basic
        with patch('sys.stdout', new=StringIO()) as fake_out:
            op.roznica(2, 1)
            r = '2-1=1\n'
            self.assertEqual(fake_out.getvalue(), r)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            op.roznica(2)
            r = '2-4=-2\n'
            self.assertEqual(fake_out.getvalue(), r)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            op.roznica()
            r = '4-5=-1\n'
            self.assertEqual(fake_out.getvalue(), r)
    # test errors and changes
        with self.assertRaises(TypeError):
            op.suma()
        op['roznica'] = [1]
        with self.assertRaises(TypeError):
            op.roznica()
        op['roznica'] = [1, 2]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            op.roznica()
            r = '1-2=-1\n'
            self.assertEqual(fake_out.getvalue(), r)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            op.roznica(5)
            r = '5-1=4\n'
            self.assertEqual(fake_out.getvalue(), r)
        op['suma'] = [1]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            op.suma(1, 2)
            r = '1+2+1=4\n'
            self.assertEqual(fake_out.getvalue(), r)
    # test return
        with patch('sys.stdout', new=StringIO()):
            op['suma'] = [1, 5]
            self.assertEqual(op.suma(1, 2), 5)
            self.assertEqual(op.suma(1, 2, 3), 1)
            self.assertEqual(op.suma(1), None)
            op['roznica'] = [5]
            self.assertEqual(op.roznica(1, 2, 3), 3)
            self.assertEqual(op.roznica(1, 2), 5)
            self.assertEqual(op.roznica(5), None)


if __name__ == '__main__':
    unittest.main()
