# Uses python3
import sys
import itertools

def partition3(A):
    total = sum(A)
    if total % 3 != 0:
        return 0
    W = total // 3
    n = len(A)

    # dp[i][j][k]: can we pick some subset of first i items so that
    # one subset sums to j, and another disjoint subset sums to k
    dp = [[[0] * (W + 1) for _ in range(W + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(n + 1):
        a = A[i - 1]
        for j in range(W + 1):
            for k in range(W + 1):
                if dp[i - 1][j][k]:
                    # don't use item `a`,
                    # then the first and second subset does not change
                    dp[i][j][k] = dp[i - 1][j][k]
                elif a <= j and dp[i - 1][j - a][k]:
                    # put in first subset
                    dp[i][j][k] = dp[i - 1][j - a][k]
                elif a <= k and dp[i - 1][j][k - a]:
                    dp[i][j][k] = dp[i - 1][j][k - a]
    return dp[n][W][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))










