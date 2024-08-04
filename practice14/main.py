class Graph:
    def __init__(self, d, c):
        self.dest = d
        self.cost = c


if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append(Graph(b, c))

    z, x = map(int, input().split())

    dist = [1_000_000_000] * (v + 1)
    last = [-1] * (v + 1)
    dist[z] = 0
    last[z] = z

    for i in range(1, v):
        for j in range(1, v + 1):
            for nxt in graph[j]:
                if dist[nxt.dest] > dist[j] + nxt.cost:
                    dist[nxt.dest] = dist[j] + nxt.cost
                    last[nxt.dest] = j

    cycle = False
    for j in range(1, v + 1):
        for nxt in graph[j]:
            if dist[nxt.dest] > dist[j] + nxt.cost:
                cycle = True
                print("GAZUA")
                exit(0)

    if dist[x] == 1_000_000_000:
        print("RAGE")
        exit(0)

    print(dist[x])
    curr = x
    path = []
    while curr != last[curr]:
        path.append(curr)
        curr = last[curr]
    path.append(z)

    for p in reversed(path):
        print(p, end=" ")
    print()
