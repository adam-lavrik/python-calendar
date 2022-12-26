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


from . import gregorian0, julianday, to_0_based, to_1_based


def is_leap(y):
    """
    Return True if year is leap, False otherwise.
    Year -1 is considered as leap, so as -5, -9, -13...
    Invalid year 0 is treated as non-leap.
    """
    return y != 0 and gregorian0.is_leap(to_0_based(y))


def leap_days(y):
    """
    Return leap day quantity in year: 0 (usual) or 1 (leap).
    """
    return int(is_leap(y))


def days_in_year(y):
    """
    Return quantity of days in year: 365 (usual), 366 (leap) or 0 (0th).
    """
    return y and gregorian0.days_in_year(to_0_based(y))


def days_in_month(m):
    """
    Return usual day quantity in month.
    Invalid input data produces meaningless result.
    """
    return gregorian0.days_in_month(m)


def days_in_year_month(y, m):
    """
    Return day quantity in year month.
    Invalid input data produces meaningless result.
    """
    return y and gregorian0.days_in_year_month(to_0_based(y), m)


def is_valid_date(y, m, d):
    """
    Return True if year, month and day represent valid Gregorian date
    (year 0 is invalid), False otherwise.
    """
    return y and gregorian0.is_valid_date(to_0_based(y), m, d)


def from_jdn(j):
    """
    Return Gregorian date of Julian day.
    """
    y, m, d = gregorian0.from_jdn(j)
    return to_1_based(y), m, d


def to_jdn(y, m, d):
    """
    Return Julian day of Gregorian date.
    Invalid input data produces meaningless result.
    """
    return gregorian0.to_jdn(to_0_based(y), m, d)


def is_valid_year_day(y, yd):
    """
    Return True if day's ordinal number within year is valid, False otherwise.
    """
    return 0 < yd <= days_in_year(y)


def from_year_day(y, yd):
    """
    Return month and day month and day by day number within year.
    Invalid input data produces meaningless result.
    """
    return gregorian0.from_year_day(to_0_based(y), yd)


def to_year_day(y, m, d):
    """
    Return day number within year by year, month and date
    (1...365 or 366 in leap year).
    Invalid input data produces meaningless result.
    """
    return gregorian0.to_year_day(to_0_based(y), m, d)


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
    return gregorian0.days_between(to_0_based(y1), m1, d1, to_0_based(y0), m0, d0)
