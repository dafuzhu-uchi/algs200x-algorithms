# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    segments.sort(key=lambda s: s.end)
    currentPoint = None
    for s in segments:
        if currentPoint is None or not (s.start <= currentPoint <= s.end):
            currentPoint = s.end
            points.append(currentPoint)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')