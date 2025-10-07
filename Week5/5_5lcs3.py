#Uses python3

import sys

def lcs3(a, b, c):
    n, m, o = len(a), len(b), len(c)
    D = [[[0] * (o+1) for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, o+1):
                if a[i-1] == b[j-1] and a[i-1] == c[k-1]:
                    D[i][j][k] = D[i-1][j-1][k-1] + 1
                else:
                    D[i][j][k] = max(
                        D[i-1][j][k],
                        D[i][j-1][k],
                        D[i][j][k-1]
                    )
    return D[n][m][o]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
