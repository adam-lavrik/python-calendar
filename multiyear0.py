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


def millennium(y):
    """
    Return year's millennium number.

    Positive/negative millenniums correspond to CE/BCE, 0th does not exist.
    CE millennium starts with year (m-1)000 and ends with year (m-1)999
    (e. g. years 0...999 = 1st millennium of current era).
    BCE millennium starts with year m000 and ends with year (m-1)001
    (e. g. years -1000...-1 = 1st millennium before current era).
    """
    return y // 1000 + (y >= 0)


def century(y):
    """
    Return year's century number.

    Positive/negative centuries correspond to CE/BCE, 0th does not exist.
    CE century starts with year (c-1)00 and ends with year (c-1)99
    (e. g. years 0...99 = 1st century of current era).
    BCE century starts with year c00 and ends with year (c-1)01
    (e. g. years -100...-1 = 1st century before current era).
    """
    return y // 100 + (y >= 0)


def decade(y):
    """
    Return year's decade number.

    CE decade starts with year d0 and ends with year d9
    (e. g. years 0...9 = 0s, 2000...2009 = 2000s of current era).
    BCE decade starts with year d0 and ends with year (d-1)1
    (e. g. years -100...-91 = 100s before current era).
    """
    return y // 10 * 10
