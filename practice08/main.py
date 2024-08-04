class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col


import queue


def isSafe(check, r, c):
    return 1 <= r <= len(check) - 1 and 1 <= c <= len(check) - 1 and check[r][c] == 0


def bfs(mars, check, q):
    sz = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q.qsize() > 0:
        p = q.get()
        r = p.row
        c = p.col
        if isSafe(check, r, c) and mars[r][c] == 1:
            check[r][c] = 1
            sz += 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                q.put(Point(nr, nc))
    return sz


if __name__ == "__main__":
    n = int(input())
    mars = [0] * (n + 1)
    for i in range(1, n + 1):
        mars[i] = [0] + list(map(int, input().split()))
    check = [[0] * (n + 1) for _ in range(n + 1)]

    q = queue.Queue()
    mx = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if mars[i][j] == 1 and check[i][j] == 0:
                q.put(Point(i, j))
                size = bfs(mars, check, q)
                mx = max(mx, size)
    print(mx)
