#!/usr/bin/env python3

import math


def solve_sock_merchant(n, ar):
    bucket_dictionary = {}
    result = 0

    for val in ar:
        if val in bucket_dictionary:
            bucket_dictionary[val].append(val)
        else:
            bucket_dictionary[val] = [val]
    # print(bucket_dictionary)

    for val in bucket_dictionary:
        result += math.floor((len(bucket_dictionary[val]) / 2))
    return result


if __name__ == '__main__':
    default_vars = {"n": 9, "ar": [10, 20, 20, 10, 10, 30, 50, 10, 20]}
    solve_sock_merchant(default_vars.get('n'), default_vars.get('ar'))
    exit(0)
