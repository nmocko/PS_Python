class Break:

    def __init__(self, hour, minute, duration=10):
        if duration == 0:
            pass
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return '---'

    def getTerm(self):
        s = self.day.name()
        s += ' ' + str(self.hour) + ':'
        if self.minute < 10:
            s += '0' + str(self.minute)
        else:
            s += str(self.minute)
        s += ' [' + str(self.duration) + ']'
        return s

