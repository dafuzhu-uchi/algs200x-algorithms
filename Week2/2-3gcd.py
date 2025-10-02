# Uses python3
import sys

def EuclidGCD(a, b):
    if b == 0:
        return a
    aa = a % b

    return EuclidGCD(b, aa)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(EuclidGCD(a, b))