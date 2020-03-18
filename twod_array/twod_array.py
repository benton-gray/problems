#!/usr/bin/env python3

import itertools

def solve_twod_array(arr):
    width = range(4)
    count = 0
    hourglass = [[1, 1, 1],
                 [0, 1, 0],
                 [1, 1, 1]]
    for i in width:
        for j in width:     
            print(list(itertools.compress(arr[i][0+j:3+j], hourglass)))
            print(list(itertools.compress(arr[i+1][0+j:3+j], hourglass[1])))
            print(list(itertools.compress(arr[i+2][0+j:3+j], hourglass[2])))
    print(arr[0][1:4])
    print(list(itertools.compress(arr[0][1:4], hourglass)))
    print(list(itertools.compress(arr, hourglass)))
    # for i, v in enumerate(arr):
    #     count +
    #     print(f"{sum(v)} -- {i}")
        # for j in width:
        #     for v in top_bot:
        #         count += i[v+j]

    # print(i)
    # print(arr)


if __name__ == '__main__':
    default_vars = [[1, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [0, 0, 2, 4, 4, 0],
                    [0, 0, 0, 2, 0, 0],
                    [0, 0, 1, 2, 4, 0]]
    solve_twod_array(default_vars)
    exit(0)
