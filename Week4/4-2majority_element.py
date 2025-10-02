# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid = (left + right) // 2
    m1 = get_majority_element(a, left, mid)
    m2 = get_majority_element(a, mid, right)
    if m1 == m2:
        return m1
    else:
        count1 = sum(1 for i in range(left, right) if a[i] == m1)
        count2 = sum(1 for i in range(left, right) if a[i] == m2)
        if count1 > (right - left) // 2:
            return m1
        elif count2 > (right - left) // 2:
            return m2

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
