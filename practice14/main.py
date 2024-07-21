class Graph:

    def __init__(self, d, c):
        self.dest = d
        self.cost = c

    def __lt__(self, other):
        return self.cost < other.cost


if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append(Graph(b, c))

    s, d = map(int, input().split())
    dist = [1_000_000_000] * (v + 1)
    last = [-1] * (v + 1)
    dist[s] = 0
    last[s] = s

    for i in range(1, v):
        for j in range(1, v + 1):
            for next in graph[j]:
                if dist[next.dest] > dist[j] + next.cost:
                    dist[next.dest] = dist[j] + next.cost
                    last[next.dest] = j

    cycle = False
    for j in range(1, v + 1):
        for next in graph[j]:
            if dist[next.dest] > dist[j] + next.cost:
                cycle = True
                break
        if cycle:
            print("GAZUA")
            exit(0)

    print(dist[d])
    curr = d
    path = []
    while curr != last[curr]:
        path.append(curr)
        curr = last[curr]
    path.append(s)
    for p in reversed(path):
        print(p, end=" ")
    print()
