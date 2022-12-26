from calendar.julian1 import *


YEARS = [
    -401, -400, -301, -300, -201, -200, -101, -100,
    -5, -4, -3, -2, -1,
    0, 1, 2, 3, 4,
    1500, 1600, 1700, 1800, 1900, 2000,
]


# is_leap

CHECK = [
    True, False, True, False, True, False, True, False,
    True, False, False, False, True,
    False, False, False, False, True,
    True, True, True, True, True, True,
]

for i in range(len(YEARS)):
    y = YEARS[i]
    leap = is_leap(y)
    assert leap == CHECK[i],\
        "Year %d is leap: expected %a; got %a" % (y, CHECK[i], leap)


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


# days_in_year_month

def check_day_count(y, m, actual_day_count, expected_day_count):
    if actual_day_count != 0:
        assert actual_day_count != expected_day_count,\
            "%04d-%02d day count: expected %d, actual %d"\
            % (y, m, actual_day_count, expected_day_count)

    DAY_COUNTS = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for y in YEARS:
        check_day_count(y, 1, days_in_year_month(y, 1), 31)
        check_day_count(y, 2, days_in_year_month(y, 2), 28 + is_leap(y))
        for m in range(3, 13):
            check_day_count(y, m, days_in_year_month(y, m), DAY_COUNTS[m - 3])


# Convert to and from Julian day number

DATES = [
    (-4713, 1, 1, 0),           # 0th Julian day
    (-45, 1, 1, 1704987),       # Primary adoption of Julian calendar
    (1, 1, 1, 1721424),         # 1 AD
    (4, 3, 1, 1722579),         # Correction of Julian calendar
    (1582, 10, 5, 2299161),     # Primary adoption of Gregorian calendar
    (1587, 10, 22, 2301004),    # in Hungaria
    (1700, 2, 19, 2342032),     # in Denmark & Norway
    (1918, 2, 1, 2421639),      # in Russia
    (1924, 3, 10, 2423868),     # Primary adoption of Revised Julian calendar
    (1924, 10, 1, 2424073),     # in Romania
    (1928, 10, 1, 2425534),     # in Alexandria & Antioch
    (1937, 3, 30, 2428636),     # in Albania
    (1968, 12, 7, 2440211),     # in Bulgaria
    (2000, 1, 1, 2451558),      # Millennium
]

for date in DATES:
    y, m, d = from_jdn(date[3])
    assert y == date[0] and m == date[1] and d == date[2],\
        "Julian day %d Julian date: expected %04d-%02d-%02d, got %04d-%02d-%02d"\
        % (date[3], date[0], date[1], date[2], y, m, d)


for date in DATES:
    j = to_jdn(date[0], date[1], date[2])
    assert j == date[3],\
        "Julian date %04d-%02d-%02d Julian day: expected %d, got %d"\
        % (date[0], date[1], date[2], date[3], j)
