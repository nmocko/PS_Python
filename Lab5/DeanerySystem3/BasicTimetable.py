from abc import ABC, abstractmethod
from typing import List
from Day import Day
from Action import Action
from Term import Term


class C:
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        r = (self.x.day.value + 10) * (self.x.hour + 2) * (self.x.minute + 12)
        return r

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.x == other.x

    def __repr__(self):
        r = (self.x.day.value + 10) * (self.x.hour + 2) * (self.x.minute + 12)
        return f"{r}"


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

    def earlier_day(self, time):

        if not TimetableWithBreaks.skipBreaks:
            self.term.duration += 10
            x = Day((self.__term.day.value - 1) % 7)
            termp = Term(x, self.__term.hour, self.__term.minute, self.__term.duration)

            if TimetableWithBreaks.can_be_transferred_to(time, termp, self.fullTime):
                self.term.duration -= 10
                termp.duration -= 10
                return Lesson(termp, self.__name, self.__teachername, self.__year)
            else:
                self.term.duration -= 10
                print("It's not possible")
                raise ValueError
        else:
            x = Day((self.__term.day.value - 1) % 7)
            termp = Term(x, self.__term.hour, self.__term.minute, self.__term.duration)

            if TimetableWithoutBreaks.can_be_transferred_to(time, termp, self.fullTime):
                return Lesson(termp, self.__name, self.__teachername, self.__year)
            else:
                print("It's not possible")
                raise ValueError

    def later_day(self, time):

        if not TimetableWithBreaks.skipBreaks:
            self.term.duration += 10

            x = Day((self.__term._Term__day.value + 1) % 7)
            termp = Term(x, self.__term.hour, self.__term.minute, self.__term.duration)

            if TimetableWithBreaks.can_be_transferred_to(time, termp, self.fullTime):
                self.term.duration -= 10
                termp.duration -= 10
                return Lesson(termp, self.__name, self.__teachername, self.__year)
            else:
                self.term.duration -= 10
                print("It's not possible")
                raise ValueError
        else:
            x = Day((self.__term._Term__day.value + 1) % 7)
            termp = Term(x, self.__term.hour, self.__term.minute, self.__term.duration)

            if TimetableWithoutBreaks.can_be_transferred_to(time, termp, self.fullTime):
                return Lesson(termp, self.__name, self.__teachername, self.__year)
            else:
                print("It's not possible")
                raise ValueError

    def later_term(self, time):
        if not TimetableWithBreaks.skipBreaks:
            self.term.duration += 10

            m = (self.__term.minute + self.__term.duration) % 60
            h = (self.__term.hour + (self.__term.minute + self.__term.duration) // 60) % 24
            d = (self.__term.day.value + (self.__term.hour + (self.__term.minute + self.__term.duration) // 60) // 24) % 7

            termp = Term(Day(d), h, m, self.__term.duration)

            self.term.duration -= 10
            termp.duration -= 10

            if TimetableWithBreaks.can_be_transferred_to(time, termp, self.fullTime):
                return Lesson(termp, self.__name, self.__teachername, self.__year)
            else:
                print("It's not possible")
                raise ValueError

        else:
            m = (self.__term.minute + self.__term.duration) % 60
            h = (self.__term.hour + (self.__term.minute + self.__term.duration) // 60) % 24
            d = (self.__term.day.value + (
                        self.__term.hour + (self.__term.minute + self.__term.duration) // 60) // 24) % 7

            termp = Term(Day(d), h, m, self.__term.duration)
            if TimetableWithoutBreaks.can_be_transferred_to(time, termp, self.fullTime):
                return Lesson(termp, self.__name, self.__teachername, self.__year)
            else:
                print("It's not possible")
            return self

    def earlier_term(self, time):

        if not TimetableWithBreaks.skipBreaks:
            self.term.duration += 10

            m = (self.__term.minute - self.__term.duration) % 60
            h = (self.__term.hour + (self.__term.minute - self.__term.duration) // 60) % 24
            d = (self.__term.day.value + (self.__term.hour + (self.__term.minute - self.__term.duration) // 60) // 24) % 7

            termp = Term(Day(d), h, m, self.__term.duration)

            self.term.duration -= 10
            termp.duration -= 10

            if TimetableWithBreaks.can_be_transferred_to(time, termp, self.fullTime):
                return Lesson(termp, self.__name, self.__teachername, self.__year)
            else:
                print("It's not possible")
                raise ValueError

        else:
            m = (self.__term.minute - self.__term.duration) % 60
            h = (self.__term.hour + (self.__term.minute - self.__term.duration) // 60) % 24
            d = (self.__term.day.value + (
                        self.__term.hour + (self.__term.minute - self.__term.duration) // 60) // 24) % 7

            termp = Term(Day(d), h, m, self.__term.duration)

            if TimetableWithoutBreaks.can_be_transferred_to(time, termp, self.fullTime):
                return Lesson(termp, self.__name, self.__teachername, self.__year)
            else:
                print("It's not possible")
                raise ValueError

    def __init__(self, term, name, teachername, year):
        self.__term = term
        self.__name = name
        self.__teachername = teachername
        self.__year = year
        if Lesson.evening_possible(self.__term):
            self.fullTime = False
        elif Lesson.day_possible(self.__term):
            self.fullTime = True
        else:
            print("We don't make lectures at this time.")
            raise TypeError



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


class BasicTimetable(ABC):

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute


    @staticmethod
    @abstractmethod
    def parse(action: List[str]) -> List[Action]:
        action_list = []
        ll = len(action)
        for j in range(ll):
            l = len(action[j])
            if l != 2:
                print("Translation argument:", action[j], "is incorrect")
                raise ValueError
            if action[j][0] != 'd' and action[j][0] != 't':
                print("Translation argument:", action[j], "is incorrect")
                raise ValueError
            if action[j][1] != '+' and action[j][1] != '-':
                print("Translation argument:", action[j], "is incorrect")
                raise ValueError

            if action[j][0] == 'd' and action[j][1] == '+':
                action_list.append(Action.DAY_LATER)
            if action[j][0] == 'd' and action[j][1] == '-':
                action_list.append(Action.DAY_EARLIER)
            if action[j][0] == 't' and action[j][1] == '+':
                action_list.append(Action.TIME_LATER)
            if action[j][0] == 't' and action[j][1] == '-':
                action_list.append(Action.TIME_EARLIER)
        return action_list

    @abstractmethod
    def perform(self, actions: List[Action]):
        l = len(actions)
        n = len(self.timetable)
        i = 0
        copy = self.timetable.copy()
        for w in copy:
            j = i
            something = None
            while j < l:
                if something != None:
                    copy[w] = something
                if actions[i] == Action.DAY_LATER:
                    something = Lesson.later_day(copy[w], self)
                if actions[i] == Action.DAY_EARLIER:
                    something = Lesson.earlier_day(copy[w], self)
                if actions[i] == Action.TIME_EARLIER:
                    something = Lesson.earlier_term(copy[w], self)
                if actions[i] == Action.TIME_LATER:
                    something = Lesson.later_term(copy[w], self)
                j += n
            del self.timetable[w]
            t = C(something.term)
            self.timetable[t] = something
            i += 1
        # for cc in self.timetable.values():
        #     j = i
        #     while j < l:
        #         if actions[i] == Action.DAY_LATER:
        #             cc = Lesson.later_day(cc, self)
        #         if actions[i] == Action.DAY_EARLIER:
        #             cc = Lesson.earlier_day(cc, self)
        #             print(cc)
        #         if actions[i] == Action.TIME_EARLIER:
        #             cc = Lesson.earlier_term(cc, self)
        #         if actions[i] == Action.TIME_LATER:
        #             cc = Lesson.later_term(cc, self)
        #         j += n
        #     i += 1

    @abstractmethod
    def get(self, term: Term) -> Lesson:
        ll = len(self.timetable)
        for i in range(ll):
            t = C(term)
            if t in self.timetable:
                return self.timetable[t]
        else:
            return None


class Break(BasicTimetable):

    def __init__(self, hour, minute, duration=10):
        if duration == 0:
            pass
        super().__init__(hour, minute)
        self.duration = duration

    def __str__(self):
        return '---'

    def getTerm(self):
        s = str(self.hour) + ':'
        if self.minute < 10:
            s += '0' + str(self.minute)
        else:
            s += str(self.minute)
        s += ' [' + str(self.duration) + ']'
        return s


class TimetableWithBreaks(BasicTimetable):

    def __init__(self):

        self.breaks = []
        h = 9
        m = 30
        for i in range(5):
            self.breaks.append(Break(h, m))
            h = h + (m + 100) // 60
            m = (m + 100) % 60
        self.breaks.append(Break(h, m))
        self.timetable = {}

    skipBreaks = False

    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:

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

        termp = Term(Day(d), h, m, term.duration)
        f = 0
        if not TimetableWithBreaks.skipBreaks:
            term.duration -= 10
        if not TimetableWithBreaks.skipBreaks:
            f = 0
            l = len(self.breaks)
            for i in range(l):
                termb = Term(term.day, self.breaks[i].hour, self.breaks[i].minute, self.breaks[i].duration)
                if Term.__eq__(termp, termb):
                    f = 1
            if f == 1:
                return False

        t = C(term)
        if t in self.timetable:
            return False
        return True

    def busy(self, term: Term) -> bool:

        m = (term.minute + term.duration) % 60
        h = (term.hour + (term.minute + term.duration) // 60) % 24
        d = (term.day.value + (term.hour + (term.minute + term.duration) // 60) // 24) % 7

        termp = Term(Day(d), h, m, term.duration)
        f = 0
        if not TimetableWithBreaks.skipBreaks:
            l = len(self.breaks)
            for i in range(l):
                termb = Term(term.day, self.breaks[i].hour, self.breaks[i].minute, self.breaks[i].duration)
                if Term.__eq__(termp, termb):
                    f = 1
            if f != 1:
                print('This term is busy 1')
                raise ValueError

        t = C(term)
        if t in self.timetable:
            print('This term is busy')
            raise ValueError
        return False

    def __str__(self):
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
                lesson = TimetableWithBreaks.get(self, terms)
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

    def put(self, lesson: Lesson) -> bool:
        if TimetableWithBreaks.can_be_transferred_to(self, lesson.term, lesson.fullTime):
            t = C(lesson.term)
            self.timetable[t] = lesson
            return True
        else:
            print("Term is busy or we don't make lectures at this time")
            raise ValueError


class TimetableWithoutBreaks(BasicTimetable):

    def __init__(self):
        self.timetable = {}

    def can_be_transferred_to(self, term: Term, fullTime: bool) -> bool:

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

        t = C(term)
        if t in self.timetable:
                return False
        return True

    def busy(self, term: Term) -> bool:

        t = C(term)
        if t in self.timetable:
            print('This term is busy')
            raise ValueError
        return False

    def __str__(self):
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
                    lesson = TimetableWithoutBreaks.get(self, terms)
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
                    lesson = TimetableWithoutBreaks.get(self, terms)
                    if lesson:
                        print(f'{lesson.name:14}', end='|')
                    else:
                        print(14 * ' ', end='|')
                print()
                h1, m1 = h2, m2
                h2, m2 = h2 + 1, 30
            print(' ' * 14, '-' * 106)

    def put(self, lesson: Lesson) -> bool:

        if TimetableWithoutBreaks.can_be_transferred_to(self, lesson.term, lesson.fullTime):
            t = C(lesson.term)
            self.timetable[t] = lesson
            return True
        else:
            print("Term is busy or we don't make lectures at this time")
            raise ValueError


if __name__ == '__main__':

    timetable = TimetableWithBreaks()
    lesson = Lesson(Term(Day.THU, 8, 0), "Programowanie", "Stanisław Polak", 2)
    if not timetable.busy(lesson.term):
        TimetableWithBreaks.put(timetable, lesson)
    lesson = Lesson(Term(Day.SUN, 16, 20), "Logika", "Krzysztof Kolumb", 4)
    if not timetable.busy(lesson.term):
        TimetableWithBreaks.put(timetable, lesson)
    lesson = Lesson(Term(Day.FRI, 11, 20), "Sieci komp.", "Julia Stasic", 1)
    if not timetable.busy(lesson.term):
        TimetableWithBreaks.put(timetable, lesson)


    act = TimetableWithBreaks.parse(["d-", "t-", "t+", "d-"])
    TimetableWithBreaks.perform(timetable, act)


    TimetableWithBreaks.__str__(timetable)

    TimetableWithBreaks.skipBreaks = True
    timetable = TimetableWithoutBreaks()
    lesson = Lesson(Term(Day.THU, 11, 0), "Programowanie", "Stanisław Polak", 2)
    if not TimetableWithoutBreaks.busy(timetable, lesson.term):
        TimetableWithoutBreaks.put(timetable, lesson)
    lesson = Lesson(Term(Day.FRI, 9, 30), "Logika", "Krzysztof Kolumb", 4)
    if not TimetableWithoutBreaks.busy(timetable, lesson.term):
        TimetableWithoutBreaks.put(timetable, lesson)
    lesson = Lesson(Term(Day.SUN, 17, 0), "Sieci komp.", "Julia Stasic", 1)
    if not TimetableWithoutBreaks.busy(timetable, lesson.term):
        TimetableWithoutBreaks.put(timetable, lesson)

    act = TimetableWithoutBreaks.parse(["t+", "t-", "t-"])
    TimetableWithoutBreaks.perform(timetable, act)

    TimetableWithoutBreaks.__str__(timetable)


