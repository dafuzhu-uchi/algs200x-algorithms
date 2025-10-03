# Uses python3
import sys


def bisect(arr: list, x: int, type: str="left") -> int:
    """
    Use binary search to find leftmost or rightmost place to insert
    which is also the number of elements in arr that < x or <= x
    :param arr: (list) ascending list
    :param x: (int) value to insert
    :param type: (str) "left" or "right"
    :return: (int) index
    """
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if type == "left":
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid
        else:
            if arr[mid] > x:
                high = mid
            else:
                low = mid + 1
    return low


def fast_count_segments(starts, ends, points):
    starts.sort()
    ends.sort()
    result = []
    for point in points:
        # how many segments start at or before the point
        cnt_start = bisect(starts, point, type="right")
        # how many segments end strictly before the point
        cnt_end = bisect(ends, point, type="left")
        # since in a pair, start<=end, so no intersections above
        result.append(cnt_start - cnt_end)
    return result


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
