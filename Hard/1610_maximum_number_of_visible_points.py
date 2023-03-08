"""

"""

from math import *
from bisect import *
def visiblePoints(points, angle, location):
    sameCnt = 0
    polarDegrees = []
    for p in points:
        if p == location:
            sameCnt += 1
        else:
            polarDegrees.append(atan2(p[1] - location[1], p[0] - location[0]))
    polarDegrees.sort()

    n = len(polarDegrees)
    polarDegrees += [deg + 2 * pi for deg in polarDegrees]

    degree = angle * pi / 180
    maxCnt = max((bisect_right(polarDegrees, polarDegrees[i] + degree) - i for i in range(n)), default=0)
    return maxCnt + sameCnt

points = [[2, 1], [2, 2], [3, 3]]
angle = 90
location = [1, 1]
print(visiblePoints(points, angle, location))
