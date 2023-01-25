class Term:

    def __init__(self, day, hour, miniute):
        self.hour = hour
        self.minute = miniute
        self.duration = 90
        self.__day = day

    def __str__(self):
        s = self.__day.name()
        s += ' ' + str(self.hour) + ':'
        if self.minute < 10:
            s += '0' + str(self.minute)
        else:
            s += str(self.minute)
        s += ' [' + str(self.duration) + ']'
        return s

    def earlierThan(self, term):
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

    def laterThan(self, term):
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

    def equals(self, term):
        if self.laterThan(term):
            return False
        if self.earlierThan(term):
            return False
        return True


