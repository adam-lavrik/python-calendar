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


from .. import julian1, revised1


def to_julian(y, m, d):
    """Return Julian date corresponding to Revised Julian date."""
    return julian1.from_jdn(revised1.to_jdn(y, m, d))


def to_revised(y, m, d):
    """Return Revised Julian date corresponding to Julian date."""
    return revised1.from_jdn(julian1.to_jdn(y, m, d))
