from typing import List
from Day import Day
from Action import Action
from Term import Term
from BasicTimetable import C
from BasicTimetable import Lesson
from BasicTimetable import BasicTimetable
from BasicTimetable import TimetableWithBreaks
from BasicTimetable import TimetableWithoutBreaks
from BasicTimetable import Break
import unittest
from io import StringIO
from unittest.mock import patch


class TestTimetableWithoutBreaks(unittest.TestCase):

    def test_break(self):
        break1 = Break(9, 20, 15)
        break2 = Break(8, 8)

        self.assertEqual(str(break1), '---')
        self.assertEqual(str(break2), '---')

        self.assertEqual(Break.getTerm(break1), '9:20 [15]')
        self.assertEqual(Break.getTerm(break2), '8:08 [10]')

    def test_BasicTimetable_parse(self):

        list1 = ['t+', 'd-', 't-', 'd+']
        list2 = ['ab']
        list3 = ['t+', 't ']

        self.assertEqual(BasicTimetable.parse(list1), [Action.TIME_LATER, Action.DAY_EARLIER, Action.TIME_EARLIER,
                                                       Action.DAY_LATER])

        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(ValueError):
                BasicTimetable.parse(list2)
            self.assertEqual(fake_out.getvalue(), 'Translation argument: ab is incorrect\n')

        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(ValueError):
                BasicTimetable.parse(list3)
            self.assertEqual(fake_out.getvalue(), 'Translation argument: t  is incorrect\n')

    def test_TimetableWithoutBreaks1(self):

        TimetableWithBreaks.skipBreaks = True
        timetable = TimetableWithoutBreaks()
        lesson = Lesson(Term(Day.THU, 11, 0), "Programowanie", "Stanisław Polak", 2)
        self.assertEqual(TimetableWithoutBreaks.busy(timetable, lesson.term), False)
        self.assertEqual(TimetableWithoutBreaks.put(timetable, lesson), True)

        lesson = Lesson(Term(Day.FRI, 9, 30), "Logika", "Krzysztof Kolumb", 4)
        self.assertEqual(TimetableWithoutBreaks.busy(timetable, lesson.term), False)
        self.assertEqual(TimetableWithoutBreaks.put(timetable, lesson), True)

        lesson = Lesson(Term(Day.SUN, 17, 0), "Sieci komp.", "Julia Stasic", 1)
        self.assertEqual(TimetableWithoutBreaks.busy(timetable, lesson.term), False)
        self.assertEqual(TimetableWithoutBreaks.put(timetable, lesson), True)

        lesson = Lesson(Term(Day.SUN, 17, 0), "Algebra", "Lech Adamus", 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(ValueError):
                self.assertEqual(TimetableWithoutBreaks.busy(timetable, lesson.term), True)
            self.assertEqual(fake_out.getvalue(), 'This term is busy\n')

        lesson = Lesson(Term(Day.THU, 11, 0), "Algebra", "Lech Adamus", 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(ValueError):
                self.assertEqual(TimetableWithoutBreaks.busy(timetable, lesson.term), True)
            self.assertEqual(fake_out.getvalue(), 'This term is busy\n')

        act = TimetableWithoutBreaks.parse(["t+", "t-", "t-"])
        TimetableWithoutBreaks.perform(timetable, act)

        self.maxDiff = None
        r = "               ----------------------------------------------------------------------------------------------------------\n" \
            "               | Poniedziałek | Wtorek       | Środa        | Czwartek     | Piątek       | Sobota       | Niedziela    | \n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "8:00 - 9:30    |              |              |              |              |Logika        |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "9:30 - 11:00   |              |              |              |              |              |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "11:00 - 12:30  |              |              |              |              |              |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "12:30 - 14:00  |              |              |              |Programowanie |              |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "14:00 - 15:30  |              |              |              |              |              |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "15:30 - 17:00  |              |              |              |              |              |              |Sieci komp.   |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "17:00 - 18:30  |              |              |              |              |              |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "18:30 - 20:00  |              |              |              |              |              |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            timetable.__str__()
            self.assertEqual(fake_out.getvalue(), r)

    def test_TimetableWithBreaks(self):

        TimetableWithBreaks.skipBreaks = False

        timetable = TimetableWithBreaks()
        lesson = Lesson(Term(Day.THU, 8, 0), "Programowanie", "Stanisław Polak", 2)
        self.assertEqual(TimetableWithBreaks.busy(timetable, lesson.term), False)
        self.assertEqual(TimetableWithBreaks.put(timetable, lesson), True)
        lesson = Lesson(Term(Day.SUN, 16, 20), "Logika", "Krzysztof Kolumb", 4)
        self.assertEqual(TimetableWithBreaks.busy(timetable, lesson.term), False)
        self.assertEqual(TimetableWithBreaks.put(timetable, lesson), True)
        lesson = Lesson(Term(Day.FRI, 11, 20), "Sieci komp.", "Julia Stasic", 1)
        self.assertEqual(TimetableWithBreaks.busy(timetable, lesson.term), False)
        self.assertEqual(TimetableWithBreaks.put(timetable, lesson), True)

        lesson = Lesson(Term(Day.SUN, 16, 20), "Algebra", "Lech Adamus", 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(ValueError):
                self.assertEqual(TimetableWithoutBreaks.busy(timetable, lesson.term), True)
            self.assertEqual(fake_out.getvalue(), 'This term is busy\n')

        lesson = Lesson(Term(Day.THU, 8, 0), "Algebra", "Lech Adamus", 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(ValueError):
                self.assertEqual(TimetableWithoutBreaks.busy(timetable, lesson.term), True)
            self.assertEqual(fake_out.getvalue(), 'This term is busy\n')

        act = TimetableWithBreaks.parse(["d-", "t-", "t+", "d-"])
        TimetableWithBreaks.perform(timetable, act)

        self.maxDiff = None

        r = "               ----------------------------------------------------------------------------------------------------------\n" \
            "               | Poniedziałek | Wtorek       | Środa        | Czwartek     | Piątek       | Sobota       | Niedziela    | \n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "8:00 - 9:30    |              |Programowanie |              |              |              |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "                     ---            ---            ---            ---            ---            ---            ---      \n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "9:40 - 11:10   |              |              |              |              |              |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "                     ---            ---            ---            ---            ---            ---            ---      \n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "11:20 - 12:50  |              |              |              |              |              |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "                     ---            ---            ---            ---            ---            ---            ---      \n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "13:00 - 14:30  |              |              |              |              |Sieci komp.   |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "                     ---            ---            ---            ---            ---            ---            ---      \n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "14:40 - 16:10  |              |              |              |              |              |              |Logika        |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "                     ---            ---            ---            ---            ---            ---            ---      \n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "16:20 - 17:50  |              |              |              |              |              |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "                     ---            ---            ---            ---            ---            ---            ---      \n" \
            "               ----------------------------------------------------------------------------------------------------------\n" \
            "18:00 - 19:30  |              |              |              |              |              |              |              |\n" \
            "               ----------------------------------------------------------------------------------------------------------\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            timetable.__str__()
            self.assertEqual(fake_out.getvalue(), r)


if __name__ == '__main__':
    unittest.main()
