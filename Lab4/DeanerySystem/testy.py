import unittest
from io import StringIO
from unittest.mock import patch
from term import Lesson
from term import Term
from day import Day


class TestLesson(unittest.TestCase):

    def test_evening_possible_test(self):
        lesson2 = Lesson(Term(Day.MON, 8, 0), "Algebra", "Andrzej Niemiec", 4)
        expected_out1 = "We don't make lectures at this time.\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            lesson3 = Lesson(Term(Day.FRI, 16, 40), "Logika", "Weronika Sztabka", 1)
            self.assertEqual(fake_out.getvalue(), expected_out1)
        lesson4 = Lesson(Term(Day.SUN, 11, 40), "Algorytmy", "Witold Zając", 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            lesson5 = Lesson(Term(Day.SUN, 20, 40), "Wykrywanie incydentów", "Klaudia Wilk", 2)
            self.assertEqual(fake_out.getvalue(), expected_out1)
        lesson6 = Lesson(Term(Day.FRI, 18, 40, 50), "Montarz filmów", "Mikołaj Grzybek", 2)

        self.assertEqual(Lesson.evening_possible(lesson2.term), False)
        self.assertEqual(Lesson.evening_possible(lesson3.term), False)
        self.assertEqual(Lesson.evening_possible(lesson4.term), True)
        self.assertEqual(Lesson.evening_possible(lesson5.term), False)
        self.assertEqual(Lesson.evening_possible(lesson6.term), True)

    def test_day_possible_test(self):
        lesson1 = Lesson(Term(Day.TUE, 11, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.MON, 8, 0), "Algebra", "Andrzej Niemiec", 4)
        expected_out1 = "We don't make lectures at this time.\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            lesson3 = Lesson(Term(Day.FRI, 16, 40), "Logika", "Weronika Sztabka", 1)
            self.assertEqual(fake_out.getvalue(), expected_out1)
        lesson4 = Lesson(Term(Day.SUN, 11, 40), "Algorytmy", "Witold Zając", 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            lesson5 = Lesson(Term(Day.SUN, 20, 40), "Wykrywanie incydentów", "Klaudia Wilk", 2)
            self.assertEqual(fake_out.getvalue(), expected_out1)
        lesson6 = Lesson(Term(Day.FRI, 18, 40, 50), "Montarz filmów", "Mikołaj Grzybek", 2)

        self.assertEqual(Lesson.day_possible(lesson1.term), True)
        self.assertEqual(Lesson.day_possible(lesson2.term), True)
        self.assertEqual(Lesson.day_possible(lesson3.term), False)
        self.assertEqual(Lesson.day_possible(lesson4.term), False)
        self.assertEqual(Lesson.day_possible(lesson5.term), False)
        self.assertEqual(Lesson.day_possible(lesson6.term), False)

    def test_earlier_day_test(self):
        lesson1 = Lesson(Term(Day.TUE, 11, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.MON, 11, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson4 = Lesson(Term(Day.SUN, 11, 40), "Algorytmy", "Witold Zając", 3)
        lesson5 = Lesson(Term(Day.SAT, 11, 40), "Algorytmy", "Witold Zając", 3)

        lessonA = lesson1.earlier_day()
        lessonB = lesson2
        self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
        self.assertEqual(lessonA.term.hour, lessonB.term.hour)
        self.assertEqual(lessonA.term.minute, lessonB.term.minute)
        self.assertEqual(lessonA.term.duration, lessonB.term.duration)
        self.assertEqual(lessonA.name, lessonB.name)
        self.assertEqual(lessonA.teachername, lessonB.teachername)
        self.assertEqual(lessonA.year, lessonB.year)

        expected_out1 = "It's not possible\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            lessonA = lesson2.earlier_day()
            lessonB = lesson2
            self.assertEqual(fake_out.getvalue(), expected_out1)
            self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
            self.assertEqual(lessonA.term.hour, lessonB.term.hour)
            self.assertEqual(lessonA.term.minute, lessonB.term.minute)
            self.assertEqual(lessonA.term.duration, lessonB.term.duration)
            self.assertEqual(lessonA.name, lessonB.name)
            self.assertEqual(lessonA.teachername, lessonB.teachername)
            self.assertEqual(lessonA.year, lessonB.year)

        lessonA = lesson4.earlier_day()
        lessonB = lesson5
        self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
        self.assertEqual(lessonA.term.hour, lessonB.term.hour)
        self.assertEqual(lessonA.term.minute, lessonB.term.minute)
        self.assertEqual(lessonA.term.duration, lessonB.term.duration)
        self.assertEqual(lessonA.name, lessonB.name)
        self.assertEqual(lessonA.teachername, lessonB.teachername)
        self.assertEqual(lessonA.year, lessonB.year)

    def test_later_day(self):
        lesson1 = Lesson(Term(Day.TUE, 11, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.WED, 11, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson4 = Lesson(Term(Day.SAT, 11, 40), "Algorytmy", "Witold Zając", 3)
        lesson5 = Lesson(Term(Day.SUN, 11, 40), "Algorytmy", "Witold Zając", 3)

        lessonA = lesson1.later_day()
        lessonB = lesson2
        self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
        self.assertEqual(lessonA.term.hour, lessonB.term.hour)
        self.assertEqual(lessonA.term.minute, lessonB.term.minute)
        self.assertEqual(lessonA.term.duration, lessonB.term.duration)
        self.assertEqual(lessonA.name, lessonB.name)
        self.assertEqual(lessonA.teachername, lessonB.teachername)
        self.assertEqual(lessonA.year, lessonB.year)

        expected_out1 = "It's not possible\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            lessonA = lesson5.later_day()
            lessonB = lesson5
            self.assertEqual(fake_out.getvalue(), expected_out1)
            self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
            self.assertEqual(lessonA.term.hour, lessonB.term.hour)
            self.assertEqual(lessonA.term.minute, lessonB.term.minute)
            self.assertEqual(lessonA.term.duration, lessonB.term.duration)
            self.assertEqual(lessonA.name, lessonB.name)
            self.assertEqual(lessonA.teachername, lessonB.teachername)
            self.assertEqual(lessonA.year, lessonB.year)

        lessonA = lesson4.later_day()
        lessonB = lesson5
        self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
        self.assertEqual(lessonA.term.hour, lessonB.term.hour)
        self.assertEqual(lessonA.term.minute, lessonB.term.minute)
        self.assertEqual(lessonA.term.duration, lessonB.term.duration)
        self.assertEqual(lessonA.name, lessonB.name)
        self.assertEqual(lessonA.teachername, lessonB.teachername)
        self.assertEqual(lessonA.year, lessonB.year)

    def test_earlier_term(self):
        lesson1 = Lesson(Term(Day.TUE, 10, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.TUE, 9, 10), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson4 = Lesson(Term(Day.SUN, 13, 10), "Algorytmy", "Witold Zając", 3)
        lesson5 = Lesson(Term(Day.SUN, 11, 40), "Algorytmy", "Witold Zając", 3)

        lessonA = lesson1.earlier_term()
        lessonB = lesson2
        self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
        self.assertEqual(lessonA.term.hour, lessonB.term.hour)
        self.assertEqual(lessonA.term.minute, lessonB.term.minute)
        self.assertEqual(lessonA.term.duration, lessonB.term.duration)
        self.assertEqual(lessonA.name, lessonB.name)
        self.assertEqual(lessonA.teachername, lessonB.teachername)
        self.assertEqual(lessonA.year, lessonB.year)

        expected_out1 = "It's not possible\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            lessonA = lesson2.earlier_term()
            lessonB = lesson2
            self.assertEqual(fake_out.getvalue(), expected_out1)
            self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
            self.assertEqual(lessonA.term.hour, lessonB.term.hour)
            self.assertEqual(lessonA.term.minute, lessonB.term.minute)
            self.assertEqual(lessonA.term.duration, lessonB.term.duration)
            self.assertEqual(lessonA.name, lessonB.name)
            self.assertEqual(lessonA.teachername, lessonB.teachername)
            self.assertEqual(lessonA.year, lessonB.year)

        lessonA = lesson4.earlier_term()
        lessonB = lesson5
        self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
        self.assertEqual(lessonA.term.hour, lessonB.term.hour)
        self.assertEqual(lessonA.term.minute, lessonB.term.minute)
        self.assertEqual(lessonA.term.duration, lessonB.term.duration)
        self.assertEqual(lessonA.name, lessonB.name)
        self.assertEqual(lessonA.teachername, lessonB.teachername)
        self.assertEqual(lessonA.year, lessonB.year)

    def test_later_term(self):
        lesson1 = Lesson(Term(Day.TUE, 17, 0), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson2 = Lesson(Term(Day.TUE, 18, 30), "Programowanie skryptowe", "Stanisław Polak", 2)
        lesson4 = Lesson(Term(Day.SUN, 13, 10), "Algorytmy", "Witold Zając", 3)
        lesson5 = Lesson(Term(Day.SUN, 14, 40), "Algorytmy", "Witold Zając", 3)

        lessonA = lesson1.later_term()
        lessonB = lesson2
        self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
        self.assertEqual(lessonA.term.hour, lessonB.term.hour)
        self.assertEqual(lessonA.term.minute, lessonB.term.minute)
        self.assertEqual(lessonA.term.duration, lessonB.term.duration)
        self.assertEqual(lessonA.name, lessonB.name)
        self.assertEqual(lessonA.teachername, lessonB.teachername)
        self.assertEqual(lessonA.year, lessonB.year)

        expected_out1 = "It's not possible\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            lessonA = lesson2.later_term()
            lessonB = lesson2
            self.assertEqual(fake_out.getvalue(), expected_out1)
            self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
            self.assertEqual(lessonA.term.hour, lessonB.term.hour)
            self.assertEqual(lessonA.term.minute, lessonB.term.minute)
            self.assertEqual(lessonA.term.duration, lessonB.term.duration)
            self.assertEqual(lessonA.name, lessonB.name)
            self.assertEqual(lessonA.teachername, lessonB.teachername)
            self.assertEqual(lessonA.year, lessonB.year)

        lessonA = lesson4.later_term()
        lessonB = lesson5
        self.assertEqual(lessonA.term._Term__day, lessonB.term._Term__day)
        self.assertEqual(lessonA.term.hour, lessonB.term.hour)
        self.assertEqual(lessonA.term.minute, lessonB.term.minute)
        self.assertEqual(lessonA.term.duration, lessonB.term.duration)
        self.assertEqual(lessonA.name, lessonB.name)
        self.assertEqual(lessonA.teachername, lessonB.teachername)
        self.assertEqual(lessonA.year, lessonB.year)

    def test_str_test(self):
        lesson1 = Lesson(Term(Day.TUE, 11, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertEqual(lesson1.__str__(), "Programowanie skryptowe (Wtorek 11:40 [90])\nDrugi rok studiów\nProwadzący: Stanisław Polak")
        lesson2 = Lesson(Term(Day.MON, 8, 0), "Algebra", "Andrzej Niemiec", 4)
        self.assertEqual(lesson2.__str__(), "Algebra (Poniedziałek 8:00 [90])\nCzwarty rok studiów\nProwadzący: Andrzej Niemiec")
        lesson4 = Lesson(Term(Day.SUN, 13, 10), "Algorytmy", "Witold Zając", 3)
        self.assertEqual(lesson4.__str__(), "Algorytmy (Niedziela 13:10 [90])\nTrzeci rok studiów\nProwadzący: Witold Zając")


if __name__ == '__main__':

    unittest.main()
