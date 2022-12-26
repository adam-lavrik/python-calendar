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


from .. import gregorian0, revised0


def to_gregorian(y, m, d):
    """Return Gregorian date corresponding to Revised Julian date."""
    return gregorian0.from_jdn(revised0.to_jdn(y, m, d))


def to_revised(y, m, d):
    """Return Revised Julian date corresponding to Gregorian date."""
    return revised0.from_jdn(gregorian0.to_jdn(y, m, d))
