# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    n = len(weights)
    items = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    items.sort(key=lambda x: x[0], reverse=True)

    for ratio, v, w in items:
        if capacity == 0:
            break
        a = min(capacity, w)
        value += ratio * a
        capacity -= a

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
