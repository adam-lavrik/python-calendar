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


def to_0_based(y):
    """
    Adjust negative years (BC) to 0-based: -1 -> 0, -2 -> -1, ...;
    remain positive years (AD) unchanged.
    """
    return y + (y < 0)


def to_1_based(y):
    """
    Adjust non-positive years to negative (BC): 0 -> -1, -1 -> -2, ...;
    remain positive years (AD) unchanged.
    """
    return y - (y <= 0)
