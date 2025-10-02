# Uses python3
import sys


def get_change(m):
    sum = 0
    for value in [10, 5, 1]:
        sum += m // value
        m -= value * (m // value)

    return sum


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
