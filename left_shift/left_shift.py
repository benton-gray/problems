#!/usr/bin/env python3

import collections


def left_shift(arr, rot):
    deq = collections.deque(arr)
    deq.rotate((rot * -1))
    return list(deq)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    rot = 1
    left_shift(arr, rot)
    exit(0)
