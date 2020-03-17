#!/usr/bin/env python3

import collections


def solve_repeated_string(n, substring):
    if substring == 'a':
        return n

    while len(substring) <= n:
        count = n - len(substring)
        substring += substring
    cnt = collections.Counter(substring[0:n])
    return cnt['a']


if __name__ == '__main__':
    default_vars = {"n": 10, "string": "aba"}
    solve_repeated_string(default_vars.get('n'), default_vars.get('string'))
    exit(0)
