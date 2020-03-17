#!/usr/bin/env python3


class sea_level():

    def __init__(self):
        self.sea_level_spot = 0
        self.valley_count = 0
        super().__init__()

    def __up(self):
        self.sea_level_spot += 1
        if self.sea_level_spot == 0:
            self.valley_count += 1

    def __down(self):
        self.sea_level_spot -= 1

    def move_logic(self, s):
        if s == "U":
            self.__up()
        if s == "D":
            self.__down()


def solve_counting_valleys(n, s):
    sea_level_manager = sea_level()
    for letter in s:
        sea_level_manager.move_logic(letter)

    # print(sea_level_manager.sea_level_spot)
    # print(sea_level_manager.sea_level_spot)
    # print(sea_level_manager.valley_count)
    return sea_level_manager.valley_count


if __name__ == '__main__':
    default_vars = {"n": 8, "ar": "UDDDUDUU"}
    solve_counting_valleys(default_vars.get('n'), default_vars.get('ar'))
    exit(0)
