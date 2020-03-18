#!/usr/bin/env python3

import collections
import math


def solve_repeated_string(n, substring):
    last_substring_size = n % len(substring)
    substring_factor = math.floor(n / len(substring))
    cnt = collections.Counter(substring)
    last_cnt = collections.Counter(substring[0:last_substring_size])
    return ((cnt['a'] * substring_factor) + last_cnt['a'])


if __name__ == '__main__':
    default_vars = {"n": 10, "string": "aba"}
    solve_repeated_string(default_vars.get('n'), default_vars.get('string'))
    exit(0)
