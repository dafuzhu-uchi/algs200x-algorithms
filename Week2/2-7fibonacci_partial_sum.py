# Uses python3
import sys


def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(m*m):
        previous, current = current, (previous + current) % m
        if (previous == 0) and (current == 1):
            return i + 1


def fibonacciLastDigit(n):
    previous, current = 0, 1
    n = n % pisanoPeriod(10)

    if n <= 1:
        return n
    else:
        for _ in range(n-1):
            previous, current = current, (previous + current) % 10
        return current


def fibonacciPartialSum(from_, to):
    result = fibonacciLastDigit(to+2) - fibonacciLastDigit(from_+1)
    if result < 0:
        return result + 10
    else:
        return result


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacciPartialSum(from_, to))