from calendar.revised0 import *


YEARS = [
    -401, -400, -301, -300, -201, -200, -101, -100,
    -5, -4, -3, -2, -1,
    0, 1, 2, 3, 4,
    1500, 1600, 1700, 1800, 1900, 2000,
]


# is_leap

CHECK = [
    False, False, False, True, False, False, False, False,
    False, True, False, False, False,
    False, False, False, False, True,
    True, False, False, False, False, True,
]

for i in range(len(YEARS)):
    y = YEARS[i]
    leap = is_leap(y)
    assert leap == CHECK[i],\
        "Year %d is leap: expected %a; got %a" % (y, CHECK[i], leap)


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
    (-4713, 11, 22, 0),         # 0th Julian day
    (-44, 1, 1, 1704990),       # Primary adoption of Julian calendar
    (1, 1, 1, 1721426),         # 1 AD
    (4, 3, 1, 1722581),         # Correction of Julian calendar
    (1582, 10, 14, 2299161),    # Primary adoption of Gregorian calendar
    (1587, 10, 31, 2301004),    # in Hungaria
    (1700, 3, 1, 2342032),      # in Denmark & Norway
    (1918, 2, 14, 2421639),     # in Russia
    (1924, 3, 23, 2423868),     # Primary adoption of Revised Julian calendar
    (1924, 10, 14, 2424073),    # in Romania
    (1928, 10, 14, 2425534),    # in Alexandria & Antioch
    (1937, 4, 12, 2428636),     # in Albania
    (1968, 12, 20, 2440211),    # in Bulgaria
    (2000, 1, 1, 2451545),      # Millennium
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


# Convert to and from year day

for y in range(2000, 2002):
    for i in range (1, days_in_year(y) + 1):
        m, d = from_year_day(y, i)
        yd = to_year_day(y, m, d)
        #print(f"{i}   {m}-{d}   {yd}")
        assert i == yd, f"Date {y}-{m}-{d} day ordinal number: expected {i}; got {yd}"
