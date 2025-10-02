# Uses python3
import sys


def pisanoPeriod(m):
    previous, current = 0, 1

    for i in range(m*m):
        previous, current = current, (previous + current) % m
        if (previous == 0) and (current == 1):
            return i + 1


def fibonacciLastDigit(n):
    n = n % pisanoPeriod(10)
    previous, current = 0, 1

    if n <= 1:
        return n
    else:
        for _ in range(n-1):
            previous, current = current, (previous + current) % 10
        return current


def fibonacciSum(n):
    last_digit = fibonacciLastDigit(n+2)
    if last_digit < 1:
        return 10 + last_digit - 1
    else:
        return last_digit - 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacciSum(n))