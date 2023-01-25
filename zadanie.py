import datetime

tab = [1580582947430, 1581271803495, 1584888980560]

for milliseconds in tab:
    seconds = milliseconds / 1000
    base_date = datetime.datetime(1970, 1, 1)
    result_date = base_date + datetime.timedelta(seconds=seconds)
    print(result_date)
