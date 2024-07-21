class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col


def isSafe(check, r, c):
    return 1 <= r <= len(check) - 1 and 1 <= c <= len(check) - 1 and check[r][c] == 0


def dfs(mars, check, stack):
    size = 0
    while stack:
        p = stack.pop()
        r = p.row
        c = p.col
        if isSafe(check, r, c) and mars[r][c] == 1:
            check[r][c] = 1
            size += 1
            stack.append(Point(r - 1, c))
            stack.append(Point(r + 1, c))
            stack.append(Point(r, c - 1))
            stack.append(Point(r, c + 1))
    return size


def dfs2(mars, check, r, c):
    if not isSafe(check, r, c) or mars[r][c] == 0: return 0
    check[r][c] = 1
    return 1 + dfs2(mars, check, r - 1, c) + dfs2(mars, check, r + 1, c) + dfs2(mars, check, r, c - 1) + dfs2(mars,
                                                                                                              check, r,
                                                                                                              c + 1)


import queue


def bfs(mars, check, q):
    sz = 0
    while q.qsize() > 0:
        p = q.get()
        r = p.row
        c = p.col
        if isSafe(check, r, c) and mars[r][c] == 1:
            check[r][c] = 1
            sz += 1
            q.put(Point(r - 1, c))
            q.put(Point(r + 1, c))
            q.put(Point(r, c - 1))
            q.put(Point(r, c + 1))

    return sz


if __name__ == "__main__":
    n = int(input())

    mars = [[0] * (n + 1) for _ in range(n + 1)]
    check = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        mars[i] = [0] + list(map(int, input().split()))

    s = []
    q = queue.Queue()

    mx = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if mars[i][j] == 1 and check[i][j] == 0:
                s.append(Point(i, j))
                q.put(Point(i, j))
                # size = dfs(mars, check, s)
                # size = bfs(mars, check, q)
                size = dfs2(mars, check, i, j)
                mx = max(size, mx)
    print(mx)
