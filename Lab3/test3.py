import unittest
from DeanerySystem.day import Day
from DeanerySystem.term import Term


class Test(unittest.TestCase):

    def test_print(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term3 = Term(Day.WED, 12, 9)
        term4 = Term(Day.SUN, 11, 0)
        self.assertEqual(term1.__str__(), "Wtorek 9:45 [90]")
        self.assertEqual(term2.__str__(), "Środa 10:15 [90]")
        self.assertEqual(term3.__str__(), "Środa 12:09 [90]")
        self.assertEqual(term4.__str__(), "Niedziela 11:00 [90]")

    def test_earlierThan(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term3 = Term(Day.WED, 12, 9)
        term4 = Term(Day.SUN, 11, 0)
        self.assertEqual(term1.earlierThan(term2), True)
        self.assertEqual(term3.earlierThan(term1), False)
        self.assertEqual(term4.earlierThan(term1), False)
        self.assertEqual(term1.earlierThan(term1), False)
        self.assertEqual(term3.earlierThan(term4), True)

    def test_laterThan(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term3 = Term(Day.WED, 12, 9)
        term4 = Term(Day.SUN, 11, 0)
        self.assertEqual(term1.laterThan(term2), False)
        self.assertEqual(term3.laterThan(term1), True)
        self.assertEqual(term4.laterThan(term1), True)
        self.assertEqual(term1.laterThan(term1), False)
        self.assertEqual(term3.laterThan(term4), False)

    def test_equals(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term3 = Term(Day.WED, 12, 9)
        term4 = Term(Day.SUN, 11, 0)
        term5 = Term(Day.SUN, 11, 0)
        self.assertEqual(term1.equals(term2), False)
        self.assertEqual(term3.equals(term1), False)
        self.assertEqual(term4.equals(term1), False)
        self.assertEqual(term1.equals(term1), True)
        self.assertEqual(term5.equals(term4), True)


if __name__ == '__main__':
    unittest.main()