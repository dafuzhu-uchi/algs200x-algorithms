# Uses python3
import sys

def lcm(a, b):
    def _gcd(a, b):
        if b == 0:
            return a
        aa = a % b
        return _gcd(b, aa)
    result = a*b // _gcd(a, b)
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))