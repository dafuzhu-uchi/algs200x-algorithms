# Uses python3

import sys
from functools import cmp_to_key


def largest_number(a):
    def _cmp(x, y):
        if x + y < y + x: return -1
        elif x + y > y + x: return 1
        else: return 0
    a = sorted(map(str, a), key=cmp_to_key(_cmp), reverse=True)
    res = ""
    for x in a:
        res += x
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

