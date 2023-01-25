from day import Day


class Term:

    def __init__(self, day, hour, miniute, duration=90):
        self.__day = day
        self.hour = hour
        self.minute = miniute
        self.duration = duration

    def __str__(self):
        s = self.__day.name()
        s += ' ' + str(self.hour) + ':'
        if self.minute < 10:
            s += '0' + str(self.minute)
        else:
            s += str(self.minute)
        s += ' [' + str(self.duration) + ']'
        return s

    def __lt__(self, term):
        if self.__day.value < term._Term__day.value:
            return True
        if self.__day.value > term._Term__day.value:
            return False
        if self.hour < term.hour:
            return True
        if self.hour > term.hour:
            return False
        if self.minute < term.minute:
            return True
        if self.minute > term.minute:
            return False
        return False

    def __gt__(self, term):
        if self.__day.value > term._Term__day.value:
            return True
        if self.__day.value < term._Term__day.value:
            return False
        if self.hour > term.hour:
            return True
        if self.hour < term.hour:
            return False
        if self.minute > term.minute:
            return True
        if self.minute < term.minute:
            return False
        return False

    def __eq__(self, term):
        if self.__lt__(term):
            return False
        if self.__gt__(term):
            return False
        if self.duration == term.duration:
            return True
        return False

    def __ge__(self, term):
        if self.__gt__(term):
            return True
        if self.__eq__(term):
            return True
        return False

    def __le__(self, term):
        if self.__lt__(term):
            return True
        if self.__eq__(term):
            return True
        return False

    def __sub__(self, term):
        n = (self._Term__day.value - term._Term__day.value) % 7
        print(n)
        duration = n * 24
        n = self.hour - term.hour
        print(n)
        duration += n
        duration *= 60
        n = self.minute - term.minute
        duration += n
        duration += term.duration

        termnew = Term(self._Term__day, self.hour, self.minute, duration)
        return termnew


class Lesson:

    @staticmethod
    def day_possible(term):
        h = term.hour + ((term.minute + term.duration) // 60)
        if (term.minute + term.duration) % 60 != 0:
            h += 1
        if term._Term__day.value < 5:
            if term.hour < 8:
                return False
            if h > 20 and term._Term__day.value < 4:
                return False
            if h > 17 and term._Term__day.value == 4:
                return False
            return True
        return False

    @staticmethod
    def evening_possible(term):
        h = term.hour + ((term.minute + term.duration) // 60)
        if (term.minute + term.duration) % 60 != 0:
            h += 1
        if term._Term__day.value > 3:
            if h > 20:
                return False
            if term._Term__day.value == 4 and term.hour < 17:
                return False
            if h > 20 and term._Term__day.value > 4:
                return False
            return True
        return False

    def earlier_day(self):
        x = Day((self.term._Term__day.value - 1) % 7)
        termp = Term(x, self.term.hour, self.term.minute, self.term.duration)
        if self.fullTime:
            if Lesson.day_possible(termp):
                return Lesson(termp, self.name, self.teachername, self.year)
            else:
                print("It's not possible")
                return self
        else:
            if Lesson.evening_possible(termp):
                return Lesson(termp, self.name, self.teachername, self.year)
            else:
                print("It's not possible")
                return self

    def later_day(self):
        x = Day((self.term._Term__day.value + 1) % 7)
        termp = Term(x, self.term.hour, self.term.minute, self.term.duration)
        if self.fullTime:
            if Lesson.day_possible(termp):
                return Lesson(termp, self.name, self.teachername, self.year)
            else:
                print("It's not possible")
                return self
        else:
            if Lesson.evening_possible(termp):
                return Lesson(termp, self.name, self.teachername, self.year)
            else:
                print("It's not possible")
                return self

    def later_term(self):

        m = (self.term.minute + self.term.duration) % 60
        h = (self.term.hour + (self.term.minute + self.term.duration) // 60) % 24
        d = (self.term._Term__day.value + (self.term.hour + (self.term.minute + self.term.duration) // 60) // 24) % 7

        termp = Term(Day(d), h, m, self.term.duration)
        if self.fullTime:
            if Lesson.day_possible(termp):
                return Lesson(termp, self.name, self.teachername, self.year)
            else:
                print("It's not possible")
                return self
        else:
            if Lesson.evening_possible(termp):
                return Lesson(termp, self.name, self.teachername, self.year)
            else:
                print("It's not possible")
                return self

    def earlier_term(self):

        m = (self.term.minute - self.term.duration) % 60
        h = (self.term.hour + (self.term.minute - self.term.duration) // 60) % 24
        d = (self.term._Term__day.value + (self.term.hour + (self.term.minute - self.term.duration) // 60) // 24) % 7

        termp = Term(Day(d), h, m, self.term.duration)

        if self.fullTime:
            if Lesson.day_possible(termp):
                return Lesson(termp, self.name, self.teachername, self.year)
            else:
                print("It's not possible")
                return self
        else:
            if Lesson.evening_possible(termp):
                return Lesson(termp, self.name, self.teachername, self.year)
            else:
                print("It's not possible")
                return self

    def __init__(self, term, name, teachername, year):
        self.term = term
        self.name = name
        self.teachername = teachername
        self.year = year
        if Lesson.evening_possible(self.term):
            self.fullTime = False
        elif Lesson.day_possible(self.term):
            self.fullTime = True
        else:
            print("We don't make lectures at this time.")

    def __str__(self):
        s = self.name + " (" + Term.__str__(self.term) + ")\n"
        if self.year == 1:
            s += "Pierwszy rok studiów"
        elif self.year == 2:
            s += "Drugi rok studiów"
        if self.year == 3:
            s += "Trzeci rok studiów"
        if self.year == 4:
            s += "Czwarty rok studiów"
        if self.year == 5:
            s += "Piąty rok studiów"
        s += "\nProwadzący: " + self.teachername
        return s


if __name__ == '__main__':

    lesson = Lesson(Term(Day.TUE, 11, 40), "Programowanie skryptowe", "Stanisław Polak", 2)
    print(lesson)
    lesson = lesson.earlier_term()
    print(lesson)
    lesson = lesson.earlier_term()
    print(lesson)
    lesson = lesson.earlier_term()
    print(lesson)
    lesson = lesson.later_term()
    print(lesson)
    lesson = lesson.later_day()
    print(lesson)
    lesson = lesson.earlier_day()
    print(lesson)
    Lesson(Term(Day.SUN, 20, 40), "Wykrywanie incydentów", "Klaudia Wilk", 2)

