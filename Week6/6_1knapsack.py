# Uses python3
import sys

def optimal_weight(W, w):
    n = len(w)
    value = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w_j in range(1, W + 1):
            value[i][w_j] = value[i - 1][w_j]
            if w[i - 1] <= w_j:
                val = 1 * w[i - 1] + value[i - 1][w_j - w[i - 1]]
                if value[i][w_j] < val:
                    value[i][w_j] = val
    return value[n][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
