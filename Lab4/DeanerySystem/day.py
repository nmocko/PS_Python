from enum import Enum


class Day(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

    def __init__(self, day):
        self.day = day

    def difference(self, day):
        x = day.value - self.day
        if -4 < x < 4:
            return x
        if x > 3:
            return x - 7
        if x < -3:
            return x + 7

    def name(self):

        if self.day == 0:
            return "Poniedziałek"
        if self.day == 1:
            return "Wtorek"
        if self.day == 2:
            return "Środa"
        if self.day == 3:
            return "Czwartek"
        if self.day == 4:
            return "Piątek"
        if self.day == 5:
            return "Sobota"
        if self.day == 6:
            return "Niedziela"


def nthDayFrom(n, day):
    x = (day.value + n) % 7
    return Day(x)

