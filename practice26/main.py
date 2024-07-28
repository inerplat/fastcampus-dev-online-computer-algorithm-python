class Point:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def dist(p, q):
    return (p.x - q.x) ** 2 + (p.y - q.y) ** 2


def brute_force(points, start, end):
    min_dist = float('inf')
    closest_pair = Pair(points[start], points[start])
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                closest_pair = Pair(points[i], points[j])
    return closest_pair


def divide(points, start, end):
    if end - start <= 3:
        return brute_force(points, start, end)

    mid = (start + end) // 2
    left_area = divide(points, start, mid)
    right_area = divide(points, mid + 1, end)

    left_dist = dist(left_area.first, left_area.second)
    right_dist = dist(right_area.first, right_area.second)

    d = min(left_dist, right_dist)
    min_pair = left_area if left_dist < right_dist else right_area

    band = []
    for i in range(start, end + 1):
        diff = points[mid].x - points[i].x
        if diff ** 2 < d:
            band.append(points[i])

    band.sort(key=lambda p: p.y)

    for i in range(len(band)):
        for j in range(i + 1, min(len(band), i + 4)):
            new_dist = dist(band[i], band[j])
            if new_dist < d:
                d = new_dist
                min_pair = Pair(band[i], band[j])

    return min_pair


def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y, i + 1))

    points.sort(key=lambda p: p.x)

    closest = divide(points, 0, n - 1)
    if closest.first.index < closest.second.index:
        print(f"{closest.first.index} {closest.second.index}")
    else:
        print(f"{closest.second.index} {closest.first.index}")


if __name__ == "__main__":
    main()
