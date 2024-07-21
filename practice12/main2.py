def init(parent, n):
    for i in range(1, n + 1):
        parent[i] = i


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    x = find(parent, a)
    y = find(parent, b)
    parent[y] = x


class Graph:
    def __init__(self, src, dest, cost):
        self.src = src
        self.dest = dest
        self.cost = cost


if __name__ == "__main__":
    n, m = map(int, input().split())
    parent = [0] * (n + 1)
    init(parent, n)
    g = []
    for _ in range(m):
        u, v, c = map(int, input().split())
        g.append(Graph(u, v, c))

    g.sort(key=lambda x: x.cost)
    ans = 0
    for i in range(m):
        if find(parent, g[i].src) != find(parent, g[i].dest):
            union(parent, g[i].src, g[i].dest)
            ans += g[i].cost

    print(ans)
