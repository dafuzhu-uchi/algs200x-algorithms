# Uses python3
def evalt(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    else: assert False

def get_min_max(i, j, ops, M, m):
    min_val, max_val = float('inf'), float('-inf')
    for k in range(i, j):
        op = ops[k]
        a = evalt(M[i][k], M[k+1][j], op)
        b = evalt(M[i][k], m[k+1][j], op)
        c = evalt(m[i][k], M[k+1][j], op)
        d = evalt(m[i][k], m[k+1][j], op)
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val

def get_maximum_value(s):
    digits = [int(s[i]) for i in range(0, len(s), 2)]
    ops = [s[i] for i in range(1, len(s), 2)]
    n = len(digits)
    M = [[0]*n for _ in range(n)]
    m = [[0]*n for _ in range(n)]
    for i in range(n):
        M[i][i] = m[i][i] = digits[i]
    for s_len in range(1, n):
        for i in range(n - s_len):
            j = i + s_len
            m[i][j], M[i][j] = get_min_max(i, j, ops, M, m)
    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))