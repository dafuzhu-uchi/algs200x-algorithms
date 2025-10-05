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


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
