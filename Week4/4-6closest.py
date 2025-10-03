#Uses python3
import sys
import math


def distance(p1, p2):
    """
    :param p1: tuple[float, float]
    :param p2: tuple[float, float]
    """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def stripClosest(strip, d):
    """
    :param strip: list[tuple[float, float]]
    :param d: float
    :return: min distance considering the strip
    """
    """Find the minimum distance within the strip"""
    min_dist = d
    # Step 4: Sort by y-axis. This step is O(n*log(n))
    strip.sort(key=lambda point: point[1])
    # Step 5: Find the smallest distance in strip
    # compare each point in the strip
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            # only comparing y-distance within d, maximum is 7 items
            # no two points occupy the same small square
            # otherwise d is not the min by previous recursive result
            if (strip[j][1] - strip[i][1]) < min_dist:
                min_dist = min(min_dist, distance(strip[i], strip[j]))
            else:
                break
    return min_dist


def minDistUtil(points, left, right):
    """Divide-and-conquer function to find min distance"""
    # Base case (<=2 points)
    if right - left <= 2:
        min_dist = float('inf')
        for i in range(left, right):  # right is excluded
            for j in range(i + 1, right):
                min_dist = min(min_dist, distance(points[i], points[j]))
        return min_dist

    # Step 1: Find middle point in the sorted array
    mid = (left + right) // 2
    mid_x = points[mid][0]

    # Step 2: Divide the array in two halves. Recursively find the min distance
    dl = minDistUtil(points, left, mid)
    dr = minDistUtil(points, mid, right)
    d = min(dl, dr)

    # Step 3: Consider the pairs that one side from left and one side from right
    # Build the strip of points within distance d around mid
    strip = []
    for i in range(left, right):
        if abs(points[i][0] - mid_x) < d:
            strip.append(points[i])

    # Find min distance inside strip
    stripDist = stripClosest(strip, d)

    return min(d, stripDist)


def minDistance(x, y):
    """
    Final result
    :param x: list[tuple[float]
    :param y: list[tuple[float]
    :return: float
    """
    n = len(x)
    points = list(zip(x, y))
    # sort the array
    points.sort(key=lambda point: point[0])
    return minDistUtil(points, 0, n)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minDistance(x, y)))









