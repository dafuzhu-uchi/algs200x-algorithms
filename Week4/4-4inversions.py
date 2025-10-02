# Uses python3
import sys


def merge_and_count(a, left, ave, right):
    """
    Cut list in half, sort and count inversions
    :return: number of inversions
    """
    l = a[left:ave]
    r = a[ave:right]
    merged = []
    count, i, j = 0, 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1
            count += len(l) - i

    merged.extend(l[i:])  # do not double count
    merged.extend(r[j:])
    a[left:right] = merged

    return count


def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, left, ave)
    number_of_inversions += get_number_of_inversions(a, ave, right)
    #write your code here
    number_of_inversions += merge_and_count(a, left, ave, right)

    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a, 0, len(a)))
