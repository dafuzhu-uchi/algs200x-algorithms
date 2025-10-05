# Uses python3
import sys

def optimal_sequence(n):
    v = [float('inf')] * (n + 1)
    v[1] = 0
    for i in range(1, n + 1):
        if i + 1 <= n and v[i + 1] > v[i] + 1:
            v[i + 1] = v[i] + 1
        if i * 2 <= n and v[i * 2] > v[i] + 1:
            v[i * 2] = v[i] + 1
        if i * 3 <= n and v[i * 3] > v[i] + 1:
            v[i * 3] = v[i] + 1

    # backtrack optimal path
    path = [n]
    cur = n
    while cur > 1:
        if cur % 3 == 0 and v[cur // 3] == v[cur] - 1:
            cur //= 3
        elif cur % 2 == 0 and v[cur // 2] == v[cur] - 1:
            cur //= 2
        else:
            cur -= 1
        path.append(cur)
    path.reverse()
    return path


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
