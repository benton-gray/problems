#!/usr/bin/env python3


def solve_twod_array(arr):
    sum = []

    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] +
                       arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
    print(max(sum))


if __name__ == '__main__':
    default_vars = [[1, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [0, 0, 2, 4, 4, 0],
                    [0, 0, 0, 2, 0, 0],
                    [0, 0, 1, 2, 4, 0]]
    solve_twod_array(default_vars)
    exit(0)
