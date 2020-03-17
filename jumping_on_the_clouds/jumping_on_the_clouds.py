#!/usr/bin/env python3


def solve_jumping_on_the_clouds(ar):
    min_jumps = 0
    skip_loop = 0

    if ar == [0]:
        return 1

    for i, val in enumerate(ar):
        print(f"{val} -- {i} -- {skip_loop} -- {min_jumps} -- {len(ar)-1}")

        if skip_loop not in [0]:
            skip_loop -= 1
            continue

        try:
            if ar[i+2] == 0:
                min_jumps += 1
                skip_loop = 1
                continue
        except IndexError:
            pass

        try:
            if ar[i+1] == 0:
                min_jumps += 1
        except IndexError:
            pass

    return min_jumps


if __name__ == '__main__':
    default_vars = {"ar": [0, 0, 1, 0, 0, 1, 0]}
    solve_jumping_on_the_clouds(default_vars.get('ar'))
    exit(0)
