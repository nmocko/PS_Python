from term import Term
from day import Day
from typing import List
from enum import Enum


class Lesson:

    @staticmethod
    def day_possible(term):
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
            return True
        return False

    @staticmethod
    def evening_possible(term):
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
            return True
        return False

    def earlier_day(self):
        x = Day((self.__term.day.value - 1) % 7)
        termp = Term(x, self.__term.hour, self.__term.minute, self.__term.duration)

        if TimetableWithoutBreaks.can_be_transferred_to(termp, self.__fullTime):
            return Lesson(termp, self.__name, self.__teachername, self.__year)
        else:
            print("It's not possible")
            return self

    def later_day(self):
        x = Day((self.__term._Term__day.value + 1) % 7)
        termp = Term(x, self.__term.hour, self.__term.minute, self.__term.duration)

        if TimetableWithoutBreaks.can_be_transferred_to(termp, self.__fullTime):
            return Lesson(termp, self.__name, self.__teachername, self.__year)
        else:
            print("It's not possible")
            return self

    def later_term(self):

        m = (self.__term.minute + self.__term.duration) % 60
        h = (self.__term.hour + (self.__term.minute + self.__term.duration) // 60) % 24
        d = (self.__term.day.value + (self.__term.hour + (self.__term.minute + self.__term.duration) // 60) // 24) % 7

        termp = Term(Day(d), h, m, self.__term.duration)

        if TimetableWithoutBreaks.can_be_transferred_to(termp, self.__fullTime):
            return Lesson(termp, self.__name, self.__teachername, self.__year)
        else:
            print("It's not possible")
        return self

    def earlier_term(self):

        m = (self.__term.minute - self.__term.duration) % 60
        h = (self.__term.hour + (self.__term.minute - self.__term.duration) // 60) % 24
        d = (self.__term.day.value + (self.__term.hour + (self.__term.minute - self.__term.duration) // 60) // 24) % 7

        termp = Term(Day(d), h, m, self.__term.duration)

        if TimetableWithoutBreaks.can_be_transferred_to(termp, self.__fullTime):
            return Lesson(termp, self.__name, self.__teachername, self.__year)
        else:
            print("It's not possible")
            return self

    def __init__(self, term, name, teachername, year):
        self.__term = term
        self.__name = name
        self.__teachername = teachername
        self.__year = year
        if Lesson.evening_possible(self.__term):
            self.__fullTime = False
        elif Lesson.day_possible(self.__term):
            self.__fullTime = True
        else:
            print("We don't make lectures at this time.")



    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, term):
        self.__term = term

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if str(name):
            self.__name = name
        else:
            self.__name = "Programowanie skryptowe"

    @property
    def teachername(self):
        return slef.__teachername

    @teachername.setter
    def teachername(self, teachername):
        if str(teachername):
            self.__teachername = teachername
        else:
            self.__teachername = "Stanislaw Polak"

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if 6 > year > 0:
            self.__year = year
        else:
            self.__year = 2


    def __str__(self):
        s = self.__name + " (" + Term.__str__(self.__term) + ")\n"
        if self.__year == 1:
            s += "Pierwszy rok studiów"
        elif self.__year == 2:
            s += "Drugi rok studiów"
        if self.__year == 3:
            s += "Trzeci rok studiów"
        if self.__year == 4:
            s += "Czwarty rok studiów"
        if self.__year == 5:
            s += "Piąty rok studiów"
        s += "\nProwadzący: " + self.__teachername
        return s


class Action(Enum):
    DAY_EARLIER = 0
    DAY_LATER = 1
    TIME_EARLIER = 2
    TIME_LATER = 3


class TimetableWithoutBreaks(object):

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

            m = (TimetableWithoutBreaks.timetable[i].term.minute + TimetableWithoutBreaks.timetable[i].term.duration) % 60
            h = (TimetableWithoutBreaks.timetable[i].term.hour + (TimetableWithoutBreaks.timetable[i].term.minute + TimetableWithoutBreaks.timetable[i].term.duration) // 60) % 24
            d = (TimetableWithoutBreaks.timetable[i].term.day.value + (TimetableWithoutBreaks.timetable[i].term.hour + (TimetableWithoutBreaks.timetable[i].term.minute + TimetableWithoutBreaks.timetable[i].term.duration) // 60) // 24) % 7
            end = Term(Day(d), h, m, TimetableWithoutBreaks.timetable[i].term.duration)

            if not((Term.__lt__(termp, TimetableWithoutBreaks.timetable[i].term) or Term.__eq__(termp, TimetableWithoutBreaks.timetable[i].term))
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


 ##########################################################

    @staticmethod
    def put(lesson: Lesson) -> bool:

        if TimetableWithoutBreaks.can_be_transferred_to(lesson.term, lesson._Lesson__fullTime):
            TimetableWithoutBreaks.timetable.append(lesson)
            return True
        else:
            return False

##########################################################

    @staticmethod
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

##########################################################

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

##########################################################

    @staticmethod
    def get(term: Term) -> Lesson:
        ll = len(TimetableWithoutBreaks.timetable)
        for i in range(ll):
            if Term.__eq__(TimetableWithoutBreaks.timetable[i].term, term):
                return TimetableWithoutBreaks.timetable[i]
        else:
            return None

    @staticmethod
    def __str__():
        print(14*' ', '-'*106)
        print(15*' ', '| ', sep='', end='')
        for i in range(7):
            print(f'{Day.name(Day(i)):13}', end='| ')
        print('\n', 15*' ', '-' * 106, sep='')
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
                        print(14*' ', end='|')
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
                        print(14*' ', end='|')
                print()
                h1, m1 = h2, m2
                h2, m2 = h2 + 1, 30
            print(' '*14, '-'*106)


if __name__ == '__main__':

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

    TimetableWithoutBreaks.__str__()


