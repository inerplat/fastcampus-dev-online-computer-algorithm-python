class Edge:
    def __init__(self, src, dest, cost):
        self.src = src
        self.dest = dest
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

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

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1

    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        c = int(data[idx])
        idx += 1
        edges.append(Edge(u, v, c))

    edges.sort()
    parent = [0] * (n + 1)
    init(parent, n)

    ans = 0
    for edge in edges:
        if find(parent, edge.src) != find(parent, edge.dest):
            ans += edge.cost
            union(parent, edge.src, edge.dest)

    root = find(parent, 1)
    for i in range(2, n + 1):
        if find(parent, i) != root:
            print(-1)
            return

    print(ans)

if __name__ == "__main__":
    main()
