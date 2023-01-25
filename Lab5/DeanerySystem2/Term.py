class Term:

    def __init__(self, day, hour, miniute, duration=90):
        self.__day = day
        self.__hour = hour
        self.__minute = miniute
        self.__duration = duration

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        values = set(item.value for item in Day)
        if day in values:
            self.__day = day
        else:
            self.__day = Day.WED

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        if 60 > minute >= 0:
            self.__minute = minute
        else:
            self.__minute = 0

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if 24 > hour >= 0:
            self.__hour = hour
        else:
            self.__hour = 8

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        if 720 > duration > 0:
            self.__duration = duration
        else:
            self.__duration = 90

    def __str__(self):
        s = self.__day.name()
        s += ' ' + str(self.__hour) + ':'
        if self.__minute < 10:
            s += '0' + str(self.__minute)
        else:
            s += str(self.__minute)
        s += ' [' + str(self.__duration) + ']'
        return s

    def __lt__(self, term):
        if self.__day.value < term.day.value:
            return True
        if self.__day.value > term.day.value:
            return False
        if self.__hour < term.hour:
            return True
        if self.__hour > term.hour:
            return False
        if self.__minute < term.minute:
            return True
        if self.__minute > term.minute:
            return False
        return False

    def __gt__(self, term):
        if self.__day.value > term.day.value:
            return True
        if self.__day.value < term.day.value:
            return False
        if self.__hour > term.hour:
            return True
        if self.__hour < term.hour:
            return False
        if self.__minute > term.minute:
            return True
        if self.__minute < term.minute:
            return False
        return False

    def __eq__(self, term):
        if self.__lt__(term):
            return False
        if self.__gt__(term):
            return False
        if self.__duration == term.duration:
            return True
        return True

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
        n = (self.__day.value - term.day.value) % 7
        print(n)
        duration = n * 24
        n = self.__hour - term.hour
        print(n)
        duration += n
        duration *= 60
        n = self.__minute - term.minute
        duration += n
        duration += term.duration

        termnew = Term(self.__day, self.__hour, self.__minute, duration)
        return termnew