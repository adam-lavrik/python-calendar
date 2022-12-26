# python-calendar

Python library for calendrical calculations based on [Julian day](https://en.wikipedia.org/wiki/Julian_day) numbers.

It is licensed under Apache 2.0 license.

## Summary

Modules with suffix `0` use 0-based year numbering (astronomical): common era starts with year 0, preceded by year −1. These calculations are slightly faster than 1-based ones, so should be preferred in use unless when dealing with historical dates before common era.


Modules with suffix `1` use 1-based year numbering (historical): common era starts with year 1, preceded by year −1; year 0 is considered invalid.

- `julianday` provides function `week_day` for calculating week day by Julian day number (1 for Monday, 2 for Tuesday, ..., 7 for Sunday).

- `multiyear#` provides calculations of millenniums, centuries and decades by given year. In 0-based variant millenniums, centuries and decades in common era begin in year x0 and end in year x9 (1st millennium is 0…999, 21st century is 2000…2099; 2020s are 2020…2029), while in 1-based variant they begin in year x1 and end in year (x+1)0 (1st millennium is 1…1000, 21st century is 2001…2100; 2020s are 2021…2030); BEFORE common era they begin in year −(x+1)0 and end in year −x1 in both variants (1st millennium BCE is −1000…−1, 2st century BCE is −200…−101; 10s BCE are −10…−1).

Calendrical modules provide the following functions:

- `is_leap` – whether given year is leap within this calendar;
- `leap_days` – leap day quantity in given year;
- `days_in_year` – day quantity in given year;
- `days_in_month` – usual day quantity in given month;
- `days_in_year_month` – day quantity in given month of given year;
- `is_valid_date` – whether given date (year, month, day) is valid within this calendar;
- `from_jdn` – date (year, month, day) by given Julian day number;
- `to_jdn` – Julian day number by given date (year, month, day);
- `is_valid_year_day` – whether given day ordinal number is valid within given year;
- `from_year_day` – month & day of given day ordinal number within given year;
- `to_year_day` – day ordinal number within year by given date (year, month, day);
- `week_day` – week day number of given date (year, month, day): see `julianday` module description;
- `days_between` – day quantity between two dates (negative if last date is earlier than first one).

Currently supported calendars:

- `julian#` — proleptic [Julian calendar](https://en.wikipedia.org/wiki/Julian_calendar) (by Sosigenes, 45 BCE);
- `gregorian#` — proleptic [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) (by Aloysius Lilius (Luigi Lilio), 1582);
- `revised#` — proleptic [Revised Julian calendar](https://en.wikipedia.org/wiki/Revised_Julian_calendar) (by Milutin Milanković (Milankovitch), 1924);

Each submodule of `convert` module provides functions for conversion between two calendars, abbreviated in the submodule's name.

## Example

```python
from calendar import multiyear0, multiyear1


print(multiyear0.millennium(2000))  # 3
print(multiyear0.century(2000))  # 21
print(multiyear0.decade(2000))  # 2000

print(multiyear1.millennium(2000))  # 2
print(multiyear1.century(2000))  # 20
print(multiyear1.decade(2000))  # 1990


from calendar import gregorian0 as gregorian


print(gregorian.is_leap(1900))  # False
print(gregorian.is_leap(1984))  # True
print(gregorian.is_leap(2000))  # True

print(gregorian.days_in_month(2))  # 28
print(gregorian.days_in_year_month(2000, 2))  # 29

print(gregorian.is_valid_date(1999, 2, 29))  # False
print(gregorian.is_valid_date(2000, 2, 29))  # True

print(gregorian.from_jdn(2451545))  # (2000, 1, 1)
print(gregorian.to_jdn(2000, 1, 1))  # 2451545

print(gregorian.is_valid_year_day(1999, 366))  # False
print(gregorian.is_valid_year_day(2000, 366))  # True

print(gregorian.from_year_day(1999, 256))  # (9, 13)
print(gregorian.from_year_day(2000, 256))  # (9, 12)

print(gregorian.to_year_day(1999, 3, 1))  # 60
print(gregorian.to_year_day(2000, 3, 1))  # 61

print(gregorian.week_day(2000, 1, 1))  # 6
print(gregorian.days_between(1900, 1, 1, 2000, 1, 1))  # 36524


from calendar.convert import gregjul0


print(gregjul0.to_gregorian(1582, 10, 5))  # (1582, 10, 15)
print(gregjul0.to_julian(1582, 10, 15))  # (1582, 10, 5)
```

(C) Adam Lavrik, 2022
