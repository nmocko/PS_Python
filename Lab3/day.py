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


def nthDayFrom(n, day):
    x = (day.value + n) % 7
    return Day(x)

