from abc import ABC, abstractmethod
from typing import List
from Term import Term
from Lesson import Lesson
from Day import Day
from Action import Action
from Break import Break


class BasicTimetable():

    @staticmethod
    @abstractmethod
    def parse(actions: List[str]) -> List[Action]:
        action_list = []
        ll = len(actions)
        for j in range(ll):
            l = len(actions[j]) - 1
            i = 0
            while i < l:
                if actions[j][i] == 'd' and actions[j][i+1] == '+':
                    action_list.append(Action.DAY_LATER)
                    i += 1
                if actions[j][i] == 'd' and actions[j][i+1] == '-':
                    action_list.append(Action.DAY_EARLIER)
                    i += 1
                if actions[j][i] == 't' and actions[j][i+1] == '+':
                    action_list.append(Action.TIME_LATER)
                    i += 1
                if actions[j][i] == 't' and actions[j][i+1] == '-':
                    action_list.append(Action.TIME_EARLIER)
                    i += 1
                i += 1
        return action_list


class TimetableWithBreaks(BasicTimetable):

    def __init__(self):

        self.breaks = []
        lesson = Lesson(Term(Day.MON, 9, 30, 90), "Programowanie skryptowe", "Stanisław Polak", 2)
        for i in range(5):
            self.breaks.append(Break(lesson.term.hour, lesson.term.minute))
            lesson = lesson.later_term()
        self.breaks.append(Break(lesson.term.hour, lesson.term.minute))

    # skipBreaks = False
    timetable = []

    @staticmethod
    def can_be_transferred_to(term: Term, fullTime: bool) -> bool:

        ok = 0
        if fullTime:
            h = term.hour + ((term.minute + term.duration) // 60)
            if (term.minute + term.duration) % 60 != 0:
                h += 1
            if term.day.value < 5:
                if term.hour < 8:
                    return False
                if h > 20 and term.day.value < 4:
                    return False
                if h > 17 and term.day.value == 4:
                    return False
                ok = 1
        else:
            h = term.hour + ((term.minute + term.duration) // 60)
            if (term.minute + term.duration) % 60 != 0:
                h += 1
            if term.day.value > 3:
                if h > 20:
                    return False
                if term.day.value == 4 and term.hour < 17:
                    return False
                if h > 20 and term.day.value > 4:
                    return False
                ok = 1
        if ok != 1:
            return False

        if not TimetableWithBreaks.skipBreaks:
            term.duration += 10

        m = (term.minute + term.duration) % 60
        h = (term.hour + (term.minute + term.duration) // 60) % 24
        d = (term.day.value + (term.hour + (term.minute + term.duration) // 60) // 24) % 7
        if not TimetableWithBreaks.skipBreaks:
            term.duration -= 10
        termp = Term(Day(d), h, m, term.duration)

        ll = len(TimetableWithBreaks.timetable)
        for i in range(ll):

            m = (TimetableWithBreaks.timetable[i].term.minute + TimetableWithBreaks.timetable[i].term.duration) % 60
            h = (TimetableWithBreaks.timetable[i].term.hour + (TimetableWithBreaks.timetable[i].term.minute + TimetableWithBreaks.timetable[i].term.duration) // 60) % 24
            d = (TimetableWithBreaks.timetable[i].term.day.value + (TimetableWithBreaks.timetable[i].term.hour + (TimetableWithBreaks.timetable[i].term.minute + TimetableWithBreaks.timetable[i].term.duration) // 60) // 24) % 7
            end = Term(Day(d), h, m, TimetableWithBreaks.timetable[i].term.duration)

            if not((Term.__lt__(termp, TimetableWithBreaks.timetable[i].term) or Term.__eq__(termp, TimetableWithBreaks.timetable[i].term))
                or (Term.__gt__(term, end) or Term.__eq__(term, end))):
                return False
        return True

    def busy(self, term: Term) -> bool:

        m = (term.minute + term.duration) % 60
        h = (term.hour + (term.minute + term.duration) // 60) % 24
        d = (term.day.value + (term.hour + (term.minute + term.duration) // 60) // 24) % 7

        termp = Term(Day(d), h, m, term.duration)
        ll = len(TimetableWithBreaks.timetable)
        f = 0
        if not TimetableWithBreaks.skipBreaks:
            l = len(self.breaks)
            for i in range(l):
                termb = Term(term.day, self.breaks[i].hour, self.breaks[i].minute, self.breaks[i].duration)

                if Term.__eq__(termp, termb):
                    f = 1
            if f != 1:
                return True

        for i in range(ll):
            if not ((Term.__lt__(term, TimetableWithBreaks.timetable[i].term) and (
                    Term.__lt__(termp, TimetableWithBreaks.timetable[i].term)
                    or Term.__eq__(termp, TimetableWithBreaks.timetable[i].term))) or (
                            Term.__gt__(term, TimetableWithBreaks.timetable[i].term)
                            and (Term.__gt__(termp, TimetableWithBreaks.timetable[i].term) or Term.__eq__(termp,
                                                                                                          TimetableWithBreaks.timetable[
                                                                                                              i].term)))):
                return True
        return False

    @staticmethod
    def __str__():
        print(14*' ', '-'*106)
        print(15*' ', '| ', sep='', end='')
        for i in range(7):
            print(f'{Day.name(Day(i)):13}', end='| ')
        print('\n', 15*' ', '-' * 106, sep='')
        h1, m1, h2, m2 = 8, 0, 9, 30
        for i in range(7):
            if m1 < 10 and m2 < 10:
                st = '{h1}:0{m1} - {h2}:0{m2}'.format(h1=h1, h2=h2, m1=m1, m2=m2)
            elif m1 < 10:
                st = '{h1}:0{m1} - {h2}:{m2}'.format(h1=h1, h2=h2, m1=m1, m2=m2)
            elif m2 < 10:
                st = '{h1}:{m1} - {h2}:0{m2}'.format(h1=h1, h2=h2, m1=m1, m2=m2)
            else:
                st = '{h1}:{m1} - {h2}:{m2}'.format(h1=h1, h2=h2, m1=m1, m2=m2)
            print(f'{st:15}', end='|')
            for j in range(7):
                terms = Term(Day(j), h1, m1, 90)
                lesson = TimetableWithBreaks.get(terms)
                if lesson:
                    print(f'{lesson.name:14}', end='|')
                else:
                    print(14 * ' ', end='|')
            print()

            h1 = h2 + (m2 + 10) // 60
            m1 = (m2 + 10) % 60
            h2 = h2 + (m2 + 100) // 60
            m2 = (m2 + 100) % 60

            if not TimetableWithBreaks.skipBreaks and i != 6:
                print(' '*14, 106*'-')
                print(' '*14, 7*'      ---      ')
            print(' ' * 14, 106 * '-')

    @staticmethod
    def get(term: Term) -> Lesson:
        ll = len(TimetableWithBreaks.timetable)
        for i in range(ll):
            if Term.__eq__(TimetableWithBreaks.timetable[i].term, term):
                return TimetableWithBreaks.timetable[i]
        else:
            return None

    @staticmethod
    def put(lesson: Lesson) -> bool:
        if TimetableWithBreaks.can_be_transferred_to(lesson.term, lesson._Lesson__fullTime):
            TimetableWithBreaks.timetable.append(lesson)
            return True
        else:
            return False

    @staticmethod
    def perform(actions: List[Action]):
        l = len(actions)
        c = len(TimetableWithBreaks.timetable)
        for i in range(l):
            if actions[i] == Action.DAY_LATER:
                TimetableWithBreaks.timetable[i % c] = Lesson.later_day(TimetableWithBreaks.timetable[i % c])
            if actions[i] == Action.DAY_EARLIER:
                TimetableWithBreaks.timetable[i % c] = Lesson.earlier_day(TimetableWithBreaks.timetable[i % c])
            if actions[i] == Action.TIME_EARLIER:
                TimetableWithBreaks.timetable[i % c] = Lesson.earlier_term(TimetableWithBreaks.timetable[i % c])
            if actions[i] == Action.TIME_LATER:
                TimetableWithBreaks.timetable[i % c] = Lesson.later_term(TimetableWithBreaks.timetable[i % c])


class TimetableWithoutBreaks(BasicTimetable):
    timetable = []

    ##########################################################
    @staticmethod
    def can_be_transferred_to(term: Term, fullTime: bool) -> bool:

        ok = 0
        if fullTime:
            h = term.hour + ((term.minute + term.duration) // 60)
            if (term.minute + term.duration) % 60 != 0:
                h += 1
            if term.day.value < 5:
                if term.hour < 8:
                    return False
                if h > 20 and term.day.value < 4:
                    return False
                if h > 17 and term.day.value == 4:
                    return False
                ok = 1
        else:
            h = term.hour + ((term.minute + term.duration) // 60)
            if (term.minute + term.duration) % 60 != 0:
                h += 1
            if term.day.value > 3:
                if h > 20:
                    return False
                if term.day.value == 4 and term.hour < 17:
                    return False
                if h > 20 and term.day.value > 4:
                    return False
                ok = 1
        if ok != 1:
            return False

        m = (term.minute + term.duration) % 60
        h = (term.hour + (term.minute + term.duration) // 60) % 24
        d = (term.day.value + (term.hour + (term.minute + term.duration) // 60) // 24) % 7
        termp = Term(Day(d), h, m, term.duration)

        ll = len(TimetableWithoutBreaks.timetable)
        for i in range(ll):

            m = (TimetableWithoutBreaks.timetable[i].term.minute + TimetableWithoutBreaks.timetable[
                i].term.duration) % 60
            h = (TimetableWithoutBreaks.timetable[i].term.hour + (
                        TimetableWithoutBreaks.timetable[i].term.minute + TimetableWithoutBreaks.timetable[
                    i].term.duration) // 60) % 24
            d = (TimetableWithoutBreaks.timetable[i].term.day.value + (TimetableWithoutBreaks.timetable[i].term.hour + (
                        TimetableWithoutBreaks.timetable[i].term.minute + TimetableWithoutBreaks.timetable[
                    i].term.duration) // 60) // 24) % 7
            end = Term(Day(d), h, m, TimetableWithoutBreaks.timetable[i].term.duration)

            if not ((Term.__lt__(termp, TimetableWithoutBreaks.timetable[i].term) or Term.__eq__(termp,
                                                                                                 TimetableWithoutBreaks.timetable[
                                                                                                     i].term))
                    or (Term.__gt__(term, end) or Term.__eq__(term, end))):
                return False
        return True

    ##########################################################

    @staticmethod
    def busy(term: Term) -> bool:

        m = (term.minute + term.duration) % 60
        h = (term.hour + (term.minute + term.duration) // 60) % 24
        d = (term.day.value + (term.hour + (term.minute + term.duration) // 60) // 24) % 7
        termp = Term(Day(d), h, m, term.duration)

        ll = len(TimetableWithoutBreaks.timetable)
        for i in range(ll):
            if not ((Term.__lt__(term, TimetableWithoutBreaks.timetable[i].term) and (
                    Term.__lt__(termp, TimetableWithoutBreaks.timetable[i].term)
                    or Term.__eq__(termp, TimetableWithoutBreaks.timetable[i].term))) or (
                            Term.__gt__(term, TimetableWithoutBreaks.timetable[i].term)
                            and (Term.__gt__(termp, TimetableWithoutBreaks.timetable[i].term) or Term.__eq__(termp,
                                                                                                             TimetableWithoutBreaks.timetable[
                                                                                                                 i].term)))):
                return True
        return False


    @staticmethod
    def __str__():
        print(14 * ' ', '-' * 106)
        print(15 * ' ', '| ', sep='', end='')
        for i in range(7):
            print(f'{Day.name(Day(i)):13}', end='| ')
        print('\n', 15 * ' ', '-' * 106, sep='')
        h1, m1, h2, m2 = 8, 0, 9, 30
        for i in range(8):
            if m1 == 0:
                str = '{h1}:00 - {h2}:30'.format(h1=h1, h2=h2)
                print(f'{str:15}', end='|')
                for j in range(7):
                    terms = Term(Day(j), h1, m1, 90)
                    lesson = TimetableWithoutBreaks.get(terms)
                    if lesson:
                        print(f'{lesson.name:14}', end='|')
                    else:
                        print(14 * ' ', end='|')
                print()
                h1, m1 = h2, m2
                h2, m2 = h2 + 2, 0
            else:
                str = '{h1}:30 - {h2}:00'.format(h1=h1, h2=h2)
                print(f'{str:15}', end='|')
                for j in range(7):
                    terms = Term(Day(j), h1, m1, 90)
                    lesson = TimetableWithoutBreaks.get(terms)
                    if lesson:
                        print(f'{lesson.name:14}', end='|')
                    else:
                        print(14 * ' ', end='|')
                print()
                h1, m1 = h2, m2
                h2, m2 = h2 + 1, 30
            print(' ' * 14, '-' * 106)

    @staticmethod
    def get(term: Term) -> Lesson:
        ll = len(TimetableWithoutBreaks.timetable)
        for i in range(ll):
            if Term.__eq__(TimetableWithoutBreaks.timetable[i].term, term):
                return TimetableWithoutBreaks.timetable[i]
        else:
            return None

    @staticmethod
    def perform(actions: List[Action]):
        l = len(actions)
        c = len(TimetableWithoutBreaks.timetable)
        for i in range(l):
            if actions[i] == Action.DAY_LATER:
                TimetableWithoutBreaks.timetable[i % c] = Lesson.later_day(TimetableWithoutBreaks.timetable[i % c])
            if actions[i] == Action.DAY_EARLIER:
                TimetableWithoutBreaks.timetable[i % c] = Lesson.earlier_day(TimetableWithoutBreaks.timetable[i % c])
            if actions[i] == Action.TIME_EARLIER:
                TimetableWithoutBreaks.timetable[i % c] = Lesson.earlier_term(TimetableWithoutBreaks.timetable[i % c])
            if actions[i] == Action.TIME_LATER:
                TimetableWithoutBreaks.timetable[i % c] = Lesson.later_term(TimetableWithoutBreaks.timetable[i % c])

    @staticmethod
    def put(lesson: Lesson) -> bool:

        if TimetableWithoutBreaks.can_be_transferred_to(lesson.term, lesson._Lesson__fullTime):
            TimetableWithoutBreaks.timetable.append(lesson)
            return True
        else:
            return False

if __name__ == '__main__':

    timetable = TimetableWithBreaks()
    lesson = Lesson(Term(Day.THU, 8, 0), "Programowanie", "Stanisław Polak", 2)
    if not timetable.busy(lesson.term):
        TimetableWithBreaks.put(lesson)
    lesson = Lesson(Term(Day.SUN, 16, 20), "Logika", "Krzysztof Kolumb", 4)
    if not timetable.busy(lesson.term):
        TimetableWithBreaks.put(lesson)
    lesson = Lesson(Term(Day.FRI, 11, 20), "Sieci komp.", "Julia Stasic", 1)
    if not timetable.busy(lesson.term):
        TimetableWithBreaks.put(lesson)
    lesson = Lesson(Term(Day.TUE, 14, 0), "Krypto.", "Julia Stasic", 1)
    if not timetable.busy(lesson.term):
        TimetableWithBreaks.put(lesson)

    l = len(TimetableWithBreaks.timetable)
    for i in range(l):
        print(TimetableWithBreaks.timetable[i].term)

    act = TimetableWithBreaks.parse(["d-", "t-", "t+", "d-"])
    TimetableWithBreaks.perform(act)

    TimetableWithBreaks.__str__()

    l = len(TimetableWithBreaks.timetable)
    for i in range(l):
        print(TimetableWithBreaks.timetable[i].term)


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

    l = len(TimetableWithoutBreaks.timetable)
    for i in range(l):
        print(TimetableWithoutBreaks.timetable[i].term)

    act = TimetableWithoutBreaks.parse(["kooa", "d+ d-", "t- t+", "t+"])
    TimetableWithoutBreaks.perform(act)

    l = len(TimetableWithoutBreaks.timetable)
    for i in range(l):
        print(TimetableWithoutBreaks.timetable[i].term)
    TimetableWithoutBreaks.__str__()

