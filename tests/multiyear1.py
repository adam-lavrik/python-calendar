from calendar.multiyear0 import *


YEARS = [
    -401, -400, -301, -300, -201, -200, -101, -100,
    -5, -4, -3, -2, -1,
    0, 1, 2, 3, 4,
    1500, 1600, 1700, 1800, 1900, 2000,
]

# century

CENTURIES = [
    -5, -4, -4, -3, -3, -2, -2, -1,
    -1, -1, -1, -1, -1,
    0, 1, 1, 1, 1,
    15, 16, 17, 18, 19, 20,
]

for i in range(len(YEARS)):
    y = YEARS[i]
    c = century(y)
    assert c == CENTURIES[i],\
        "Year %d century: expected %d; got %d" % (y, c, CENTURIES[i])


# decade

DECADES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def check_decade(y, actual_decade, expected_decade):
    assert actual_decade == expected_decade,\
        "Year %d decade: expected %d; got %d"\
        % (y, expected_decade, actual_decade)

y = -100
d = 0
while y <= 100:
    check_decade(y, decade(y), DECADES[d])
    y += 1
    check_decade(y, decade(y), DECADES[d])
    y += 8
    check_decade(y, decade(y), DECADES[d])
    y += 1
    if y == 0:
        y += 1
    d += 1
