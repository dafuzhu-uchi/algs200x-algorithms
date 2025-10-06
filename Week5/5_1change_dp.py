# Uses python3
import sys


def get_change(m):
    coins = [1, 3, 4]
    dp = [float('inf')] * (m + 1)
    dp[0] = 0
    for coin in coins:
        for amount in range(coin, m + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    return dp[m] if dp[m] != float('inf') else -1


def get_change2(m):
    # margin case
    if m == 1:
        return 1

    # Bottom up
    v = [float('inf')] * (m + 1)
    v[0] = 0
    coins = [1, 3, 4]
    for i in range(1, m + 1):
        for coin in coins:
            if i + coin <= m and v[i + coin] > v[i] + 1:
                v[i + coin] = v[i] + 1

    # Top down
    path = [m]
    cur = m
    while cur > 1:
        for coin in reversed(coins):  # tie-breaking order if needed
            if cur - coin >= 0 and v[cur - coin] == v[cur] - 1:
                cur -= coin
                path.append(cur)
                break

    path.reverse()

    return len(path) - 1


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change2(m))

