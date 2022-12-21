Python library for calendaric calculations based on [Julian day](https://en.wikipedia.org/wiki/Julian_day) numbers.

Modules with suffix 0 use 0-based year numbering (astronomical): common era starts with year 0, which is preceded by year -1. These calculations are slightly faster than 1-based ones, so should be preferable in use unless dealing with dates BCE.

Modules with suffix 1 use 1-based year numbering (chronological): common era starts with year 1, which is preceded by year -1; year 0 is considered as invalid.

- `julianday` provides function `week_day` which calculates week day by Julian day number (1 for Monday, 2 for Tuesday, ..., 7 for Sunday).

- `multiyear`*N* provides calculations of centuries and decades by given year. In 0-based variant common era centuries/decades start in year x0 and end in year x9 (21st century is 2000…2099; 2020s are 2020…2029), while in 1-based variant they start in year x1 and end in year (x+1)0 (21st century is 2001…2100; 2020s are 2021…2030); Centuries/decades BEFORE common era start in year -(x+1)0 and end in year -x1 in both variants (2st century BCE is -200…-101; 10s BCE are -10…-1).

Calendaric modules provide the following functions:

- `is_leap_year` – whether given year is leap within current calendar;
- `leap_days` – leap day quantity in given year;
- `days_in_year` – day quantity in given year;
- `days_in_month` – usual day quantity in given month;
- `days_in_year_month` – day quantity in given month of given year;
- `is_valid_date` – whether given date (year, month, day) is valid within current calendar;
- `from_jdn` – date (year, month, day) by given Julian day number;
- `to_jdn` – Julian day number by given date (year, month, day);
- `is_valid_year_day` – whether given day ordinal number is valid within given year;
- `from_year_day` – month & day of given day ordinal number within given year;
- `to_year_day` – day ordinal number within year by given date (year, month, day);
- `week_day` – week day number of given date (year, month, day): see `julianday` module description;
- `days_between` – day quantity between two dates (negative if last date is earlier than first one).

Currently supported calendars:

- `julian`*N* — [Julian](https://en.wikipedia.org/wiki/Julian_calendar) (by Sosigenes, 45 BCE);
- `gregorian`*N* — [Gregorian](https://en.wikipedia.org/wiki/Gregorian_calendar) (by Aloysius Lilius (Luigi Lilio), 1582);
- `revised`*N* — [Revised Julian](https://en.wikipedia.org/wiki/Revised_Julian_calendar) (by Milutin Milanković (Milankovitch), 1924);
