def ccw(o, a, b):
    return (o.x * a.y + a.x * b.y + b.x * o.y) - (o.y * a.x + a.y * b.x + b.y * o.x)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        ccw_value = ccw(base_point, self, other)
        if ccw_value == 0:
            distance_self = abs(self.x - base_point.x) + abs(self.y - base_point.y)
            distance_other = abs(other.x - base_point.x) + abs(other.y - base_point.y)
            return distance_self < distance_other
        return ccw_value > 0

base_point = None


def convex_hull(points):
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    return lower


def main():
    n = int(input())
    points = []

    base_index = 0

    for i in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))
        if y < points[base_index].y or (y == points[base_index].y and x < points[base_index].x):
            base_index = i

    points[0], points[base_index] = points[base_index], points[0]
    global base_point
    base_point = points[0]

    points = [base_point] + sorted(points[1:])
    hull = convex_hull(points)
    print(n - len(hull))


if __name__ == "__main__":
    main()
