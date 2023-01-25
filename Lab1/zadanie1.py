from fractions import Fraction


class MyException(Exception):
    pass


def suma(arg1, arg2):

    if isinstance(arg1, str):
        r = 0
        f = 0
        for i in arg1:
            if i == '.':
                f += 1
                if f > 1:
                    r = 1
            elif '0' > i or i > '9':
                r = 1
        if r == 1:
            raise MyException
        else:
            arg1 = float(arg1)

    if isinstance(arg2, str):
        r = 0
        f = 0
        for i in arg2:
            if i == '.':
                f += 1
                if f > 1:
                    r = 1
            elif '0' > i or i > '9':
                r = 1
        if r == 1:
            raise MyException
        else:
            arg2 = float(arg2)
    if isinstance(arg1, (complex, str, Fraction, int, float)) and isinstance(arg2, (complex, str, Fraction, int, float)):
        a = arg1 + arg2
    else:
        raise MyException
    return a


if __name__ == '__main__':
    wynik = suma(1, 4)
    print("suma = <", wynik, ">")

    print("__name__ = ", __name__)