# Uses python3
import sys


def optimal_summands(n):
    summands = []
    currentPrize = 1
    total = 0

    for i in range(n):
        if 2 * currentPrize + 1 <= n - total:
            summands.append(currentPrize)
            total += currentPrize
            currentPrize += 1
        else:
            summands.append(n - total)
            break

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
