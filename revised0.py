"""
Copyright 2022 Adam Lavrik <lavrik.adam@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific
language governing permissions and limitations under the License.
"""


from . import julianday


def is_leap_year(y):
    """
    Return True if given year is leap, False otherwise.
    Year 0 is considered as leap, so as -4, -8, -12, ...
    """
    return not ((y & 3 != 0) or (y % 100 == 0) and (200 != y % 900 != 600))


def leap_days(y):
    """
    Return leap day quantity in year: 0 (usual) or 1 (leap).
    """
    return int(is_leap_year(y))


def days_in_year(y):
    """
    Return day quantity in year: 365 (usual) or 366 (leap).
    """
    return 365 + leap_days(y)


def days_in_month(m):
    """
    Return usual day quantity in month.
    Invalid input data produces meaningless result.
    """
    # Bit pairs of constant below represent quantity of days exceeding 4 weeks
    # for each month (0...3).
    return (0b11_10_11_10_11_11_10_11_10_11_00_11_00 >> (m + m) & 3) + 28


def days_in_year_month(y, m):
    """
    Return day quantity in year month.
    Invalid input data produces meaningless result.
    """
    return days_in_month(m) + (m == 2 and leap_days(y))


def is_valid_date(y, m, d):
    """
    Return True if year, month and day represent valid Revised Julian date
    (year 0 is valid), False otherwise.
    """
    return 0 < m < 13 and 0 < d <= days_in_year_month(y, m)


def from_jdn(j):
    """
    Return Revised Julian date of Julian day.
    """
    d = (j - 1721120) * 9 + 2
    y = d // 328718
    d = d % 328718 // 9 * 100 + 99
    m = d // 36525
    d = d % 36525 // 100 * 5 + 2
    y = y * 100 + m
    m = d // 153
    d = d % 153 // 5 + 1
    if m > 9:
        y += 1
        m -= 9
    else:
        m += 3
    return y, m, d


def to_jdn(y, m, d):
    """
    Return Julian day of Revised Julian date.
    Invalid input data produces meaningless result.
    """
    if m < 3:  # January or February
        y -= 1
        m += 9
    else:
        m -= 3
    return (
        (y // 100 * 328718 + 6) // 9 + y % 100 * 36525 // 100 +
        (m * 153 + 2) // 5 + d + 1721119
    )


def is_valid_year_day(y, yd):
    """
    Return True if day's ordinal number within year is valid, False otherwise.
    """
    return 0 < yd <= days_in_year(y)


def from_year_day(y, yd):
    """
    Return month and day by day number within year.
    Invalid input data produces meaningless result.
    """
    # y becomes 0 if day is in January,
    # otherwise 1 if year is leap, or 2 if year is non-leap.
    y = yd >> 5 and 2 - leap_days(y)
    m = ((yd + y) * 18 + 539) // 550
    return m, yd - m * 275 // 9 + (m > 2) * y + 30


def to_year_day(y, m, d):
    """
    Return day number within year by year, month and date
    (1...365 or 366 in leap year).
    Invalid input data produces meaningless result.
    """
    return m * 275 // 9 - (2 - leap_days(y)) * (m > 2) + d - 30


def week_day(y, m, d):
    """
    Return week day number of date (1 = Monday, ...,  7 = Sunday).
    Invalid input data produces meaningless result.
    """
    return julianday.week_day(to_jdn(y, m, d))


def days_between(y0, m0, d0, y1, m1, d1):
    """
    Return day quantity between two dates
    (negative if last date is earlier than first one).
    Invalid input data produces meaningless result.
    """
    return to_jdn(y1, m1, d1) - to_jdn(y0, m0, d0)
