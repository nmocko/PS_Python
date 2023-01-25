from term import Term
from day import Day
from typing import List
from enum import Enum
from lesson import Lesson
from lesson import Action
from lesson import TimetableWithoutBreaks
import unittest
from io import StringIO
from unittest.mock import patch


class TestTimetableWithoutBreaks(unittest.TestCase):

    def test_busy(self):

        TimetableWithoutBreaks.timetable = [Lesson(Term(Day(1), 8, 0), "Algerbra", "Maciej Rak", 2),
                                            Lesson(Term(Day(6), 17, 0), "Logika", "Agnieszka Pająk", 3),
                                            Lesson(Term(Day(6), 15, 0), "Programowanie", "Stanisław Polak", 1),
                                            Lesson(Term(Day(5), 18, 0), "W-F", "Mariusz Piłka", 1)]
        lesson = Lesson(Term(Day.THU, 11, 0), "Programowanie", "Stanisław Polak", 2)
        self.assertEqual(TimetableWithoutBreaks.busy(lesson.term), False)
        lesson = Lesson(Term(Day.THU, 12, 30), "Logika", "Krzysztof Kolumb", 4)
        self.assertEqual(TimetableWithoutBreaks.busy(lesson.term), False)
        lesson = Lesson(Term(Day.SUN, 17, 0), "Krypto.", "Julia Stasic", 1)
        self.assertEqual(TimetableWithoutBreaks.busy(lesson.term), True)
        lesson = Lesson(Term(Day.SUN, 16, 0), "Krypto.", "Julia Stasic", 1)
        self.assertEqual(TimetableWithoutBreaks.busy(lesson.term), True)

    def test_put(self):
        TimetableWithoutBreaks.timetable = []
        tab = []
        lesson = Lesson(Term(Day.THU, 11, 0), "Programowanie", "Stanisław Polak", 2)
        TimetableWithoutBreaks.put(lesson)
        tab.append(lesson)
        self.assertEqual(TimetableWithoutBreaks.timetable, tab)
        lesson = Lesson(Term(Day.THU, 12, 30), "Logika", "Krzysztof Kolumb", 4)
        TimetableWithoutBreaks.put(lesson)
        tab.append(lesson)
        self.assertEqual(TimetableWithoutBreaks.timetable, tab)
        lesson = Lesson(Term(Day.SUN, 17, 0), "Krypto.", "Julia Stasic", 1)
        TimetableWithoutBreaks.put(lesson)
        tab.append(lesson)
        self.assertEqual(TimetableWithoutBreaks.timetable, tab)

    def test_parse(self):

        acct = [Action.DAY_LATER, Action.DAY_EARLIER, Action.TIME_EARLIER, Action.TIME_LATER, Action.TIME_LATER]
        self.assertEqual(TimetableWithoutBreaks.parse(["kooa", "d+ d-", "t- t+", "t+"]), acct)
        acct = [Action.TIME_EARLIER, Action.DAY_EARLIER, Action.TIME_EARLIER, Action.TIME_LATER]
        self.assertEqual(TimetableWithoutBreaks.parse(["ko t-oa", "d-", "t- !!!t+"]), acct)
        acct = [Action.DAY_EARLIER]
        self.assertEqual(TimetableWithoutBreaks.parse(["d", "d-", "-d"]), acct)
        acct = [Action.DAY_EARLIER]
        self.assertEqual(TimetableWithoutBreaks.parse(["d-"]), acct)
        acct = []
        self.assertEqual(TimetableWithoutBreaks.parse(["kkk"]), acct)

    def test_get(self):
        TimetableWithoutBreaks.timetable = [Lesson(Term(Day(1), 8, 0), "Algerbra", "Maciej Rak", 2),
                                            Lesson(Term(Day(6), 17, 0), "Logika", "Agnieszka Pająk", 3),
                                            Lesson(Term(Day(6), 15, 0), "Programowanie", "Stanisław Polak", 1),
                                            Lesson(Term(Day(5), 18, 0), "W-F", "Mariusz Piłka", 1)]
        term1 = Term(Day(1), 8, 0)
        self.assertEqual(TimetableWithoutBreaks.get(term1), TimetableWithoutBreaks.timetable[0])
        term2 = Term(Day(6), 15, 0)
        self.assertEqual(TimetableWithoutBreaks.get(term2), TimetableWithoutBreaks.timetable[2])
        term3 = Term(Day(1), 9, 0)
        self.assertEqual(TimetableWithoutBreaks.get(term3), None)
        term4 = Term(Day(5), 18, 0)
        self.assertEqual(TimetableWithoutBreaks.get(term4), TimetableWithoutBreaks.timetable[3])
        term5 = Term(Day(2), 8, 0)
        self.assertEqual(TimetableWithoutBreaks.get(term5), None)

    def test_can_be_transferred_to(self):
        TimetableWithoutBreaks.timetable = [Lesson(Term(Day(1), 8, 0), "Algerbra", "Maciej Rak", 2),
                                            Lesson(Term(Day(6), 17, 0), "Logika", "Agnieszka Pająk", 3),
                                            Lesson(Term(Day(6), 15, 0), "Programowanie", "Stanisław Polak", 1),
                                            Lesson(Term(Day(5), 18, 0), "W-F", "Mariusz Piłka", 1)]
        term = Term(Day(1), 8, 0)
        self.assertEqual(TimetableWithoutBreaks.can_be_transferred_to(term, True), False)
        term = Term(Day(1), 9, 0)
        self.assertEqual(TimetableWithoutBreaks.can_be_transferred_to(term, True), False)
        term = Term(Day(1), 10, 0)
        self.assertEqual(TimetableWithoutBreaks.can_be_transferred_to(term, True), True)
        term = Term(Day(4), 15, 0)
        self.assertEqual(TimetableWithoutBreaks.can_be_transferred_to(term, False), False)
        term = Term(Day(6), 12, 0)
        self.assertEqual(TimetableWithoutBreaks.can_be_transferred_to(term, False), True)
        term = Term(Day(6), 15, 30)
        self.assertEqual(TimetableWithoutBreaks.can_be_transferred_to(term, False), False)

    def test_str_(self):

        self.maxDiff = None
        result = """               ----------------------------------------------------------------------------------------------------------
               | Poniedziałek | Wtorek       | Środa        | Czwartek     | Piątek       | Sobota       | Niedziela    | 
               ----------------------------------------------------------------------------------------------------------
8:00 - 9:30    |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
9:30 - 11:00   |              |              |              |Logika        |              |              |              |
               ----------------------------------------------------------------------------------------------------------
11:00 - 12:30  |              |              |              |              |Programowanie |              |              |
               ----------------------------------------------------------------------------------------------------------
12:30 - 14:00  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
14:00 - 15:30  |              |              |              |              |              |              |Sieci komp.   |
               ----------------------------------------------------------------------------------------------------------
15:30 - 17:00  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
17:00 - 18:30  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
18:30 - 20:00  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
"""

        TimetableWithoutBreaks.timetable = [Lesson(Term(Day.FRI, 11, 0), "Programowanie", "Stanisław Polak", 2),
                                            Lesson(Term(Day.THU, 9, 30), "Logika", "Krzysztof Kolumb", 4),
                                            Lesson(Term(Day.SUN, 14, 0), "Sieci komp.", "Julia Stasic", 1)]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            TimetableWithoutBreaks.__str__()
            self.assertEqual(fake_out.getvalue(), result)

        result = """               ----------------------------------------------------------------------------------------------------------
               | Poniedziałek | Wtorek       | Środa        | Czwartek     | Piątek       | Sobota       | Niedziela    | 
               ----------------------------------------------------------------------------------------------------------
8:00 - 9:30    |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
9:30 - 11:00   |              |              |              |Logika        |              |              |              |
               ----------------------------------------------------------------------------------------------------------
11:00 - 12:30  |              |              |              |              |Programowanie |              |              |
               ----------------------------------------------------------------------------------------------------------
12:30 - 14:00  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
14:00 - 15:30  |              |              |              |              |              |              |Sieci komp.   |
               ----------------------------------------------------------------------------------------------------------
15:30 - 17:00  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
17:00 - 18:30  |Ekonomia      |              |              |              |              |              |Krypto.       |
               ----------------------------------------------------------------------------------------------------------
18:30 - 20:00  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
"""

        TimetableWithoutBreaks.timetable = [Lesson(Term(Day.FRI, 11, 0), "Programowanie", "Stanisław Polak", 2),
                                        Lesson(Term(Day.THU, 9, 30), "Logika", "Krzysztof Kolumb", 4),
                                        Lesson(Term(Day.SUN, 14, 0), "Sieci komp.", "Julia Stasic", 1),
                                        Lesson(Term(Day.SUN, 17, 0), "Krypto.", "Julia Stasic", 1),
                                        Lesson(Term(Day.MON, 17, 0), "Ekonomia", "Julia Stasic", 1)]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            TimetableWithoutBreaks.__str__()
            self.assertEqual(fake_out.getvalue(), result)

    def test_perform(self):

        self.maxDiff = None
        TimetableWithoutBreaks.timetable = [Lesson(Term(Day.FRI, 11, 0), "Programowanie", "Stanisław Polak", 2),
                                            Lesson(Term(Day.THU, 9, 30), "Logika", "Krzysztof Kolumb", 4),
                                            Lesson(Term(Day.SUN, 14, 0), "Sieci komp.", "Julia Stasic", 1),
                                            Lesson(Term(Day.SUN, 17, 0), "Krypto.", "Julia Stasic", 1),
                                            Lesson(Term(Day.MON, 17, 0), "Ekonomia", "Julia Stasic", 1)]


        acct = [Action.DAY_LATER, Action.DAY_EARLIER, Action.TIME_EARLIER, Action.TIME_LATER, Action.TIME_LATER, Action.TIME_LATER, Action.TIME_LATER]

        TimetableWithoutBreaks.perform(acct)

        result = """               ----------------------------------------------------------------------------------------------------------
               | Poniedziałek | Wtorek       | Środa        | Czwartek     | Piątek       | Sobota       | Niedziela    | 
               ----------------------------------------------------------------------------------------------------------
8:00 - 9:30    |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
9:30 - 11:00   |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
11:00 - 12:30  |              |              |Logika        |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
12:30 - 14:00  |              |              |              |              |Programowanie |              |Sieci komp.   |
               ----------------------------------------------------------------------------------------------------------
14:00 - 15:30  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
15:30 - 17:00  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
17:00 - 18:30  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
18:30 - 20:00  |Ekonomia      |              |              |              |              |              |Krypto.       |
               ----------------------------------------------------------------------------------------------------------
"""

        with patch('sys.stdout', new=StringIO()) as fake_out:
            TimetableWithoutBreaks.__str__()
            self.assertEqual(fake_out.getvalue(), result)


    def full_test(self):
        lesson = Lesson(Term(Day.THU, 11, 0), "Programowanie", "Stanisław Polak", 2)
        if not TimetableWithoutBreaks.busy(lesson.term):
            TimetableWithoutBreaks.put(lesson)
        lesson = Lesson(Term(Day.FRI, 9, 30), "Logika", "Krzysztof Kolumb", 4)
        if not TimetableWithoutBreaks.busy(lesson.term):
            TimetableWithoutBreaks.put(lesson)
        lesson = Lesson(Term(Day.SUN, 17, 0), "Sieci komp.", "Julia Stasic", 1)
        if not TimetableWithoutBreaks.busy(lesson.term):
            TimetableWithoutBreaks.put(lesson)
        lesson = Lesson(Term(Day.SUN, 17, 0), "Krypto.", "Julia Stasic", 1)
        if not TimetableWithoutBreaks.busy(lesson.term):
            TimetableWithoutBreaks.put(lesson)

        act = TimetableWithoutBreaks.parse(["kooa", "d+ d-", "t- t+", "t+"])
        TimetableWithoutBreaks.perform(act)

        result = """               ----------------------------------------------------------------------------------------------------------
               | Poniedziałek | Wtorek       | Środa        | Czwartek     | Piątek       | Sobota       | Niedziela    | 
               ----------------------------------------------------------------------------------------------------------
8:00 - 9:30    |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
9:30 - 11:00   |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
11:00 - 12:30  |              |              |              |Logika        |              |              |              |
               ----------------------------------------------------------------------------------------------------------
12:30 - 14:00  |              |              |              |              |Programowanie |              |              |
               ----------------------------------------------------------------------------------------------------------
14:00 - 15:30  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
15:30 - 17:00  |              |              |              |              |              |              |Sieci komp.   |
               ----------------------------------------------------------------------------------------------------------
17:00 - 18:30  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
18:30 - 20:00  |              |              |              |              |              |              |              |
               ----------------------------------------------------------------------------------------------------------
"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            TimetableWithoutBreaks.__str__()
            self.assertEqual(fake_out.getvalue(), result)


if __name__ == '__main__':

    unittest.main()
