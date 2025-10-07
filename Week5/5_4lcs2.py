#Uses python3

import sys

def lcs2(a, b):
    n, m = len(a), len(b)
    D = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                D[i][j] = D[i-1][j-1] + 1
                # I first wrote `D[i][j] = max(D[i][j-1], D[i-1][j]) + 1`
                # which fails the test. A good counterexample is,
                # a = [1, 3, 4, 1]
                # b = [3, 4, 1, 2, 1, 3]
                # or simply input: 4 1 3 4 1 6 3 4 1 2 1 3
            else:
                D[i][j] = max(D[i][j-1], D[i-1][j])
    return D[n][m]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
