towar = { "mango": 100, "ogorek" : 200, "marchweka" : 150, "kurczak" : 200, "rak" : 120, "mleko" : 122}
historia = []
f = 0

def dane():

    try:
        czynnosc, a, b, c = input("Sprzedarz/Kupno/Zwrucone/Ctrl+d:, Nazwa towaru, ilosc (kg), nazwisko: ").split()
        return czynnosc, a, b, c

    except EOFError:
        print("Historia: ", historia, "\n", "Towar: ", towar)
        exit(0)


def sklep(czynnosc, a, b, c):

    if czynnosc == "Kupno":

        if a in towar:
            x = towar[a]
            if int(b) <= x:
                towar[a] -= int(b)
                historia.append([a, b, c])
                print(historia)
                return "OK, kupiles"
            else:
                return "Za mało produktów na stanie"
        else:
            return "Nie ma takiego produktu"

    if czynnosc == "Sprzedarz":
        if a in towar:
            x = towar[a]
            towar[a] = int(x) + int(b)
            return "Sprzedane"
        else:
            towar[a] = int(b)
            return "Nowy towar w sklepie, sprzedane"

    if czynnosc == "Zwrot":
        f = len(historia)
        for i in range(f):
            print(historia[i])
            if historia[i][2] == c and historia[i][0] == a:
                if (int(b) <= int(historia[i][1])):
                    x = towar[a]
                    towar[a] = int(b) + int(x)
                    historia[i][1] = int(historia[i][1]) - int(b)
                    return "Zwrucone"
                else:
                    return "Zwruciles za duzo"
        else:
            return "Nie kupiles tego"
    else:
        return "Nie ma takiej komendy"


if __name__ == "__main__":
    while True:

        czynnosc, a, b, c = dane()

        print(sklep(czynnosc, a, b, c))
