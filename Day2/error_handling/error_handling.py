import datetime
import random

day = random.choice(['Eleventh', 11])

try:
    date = 'September ' + day
except TypeError:
    date = datetime.date(2018, 9, day)
else:
    day += '2018'
finally:
    print(date)