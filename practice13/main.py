import queue


class Graph:
    def __init__(self, d, t):
        self.dest = d
        self.time = t

    def __lt__(self, other):
        return self.time < other.time


if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append(Graph(b, c))

    s, d = map(int, input().split())
    dist = [1_000_000_000] * (v + 1)
    visited = [False] * (v + 1)
    last = [0] * (v + 1)

    pq = queue.PriorityQueue()
    pq.put(Graph(s, 0))
    dist[s] = 0
    last[s] = s
    while pq.qsize():
        cur = pq.get()
        u = cur.dest
        if visited[u]:
            continue
        visited[u] = True
        for g in graph[u]:
            v = g.dest
            if dist[v] > dist[u] + g.time:
                dist[v] = dist[u] + g.time
                last[v] = u
                pq.put(Graph(v, dist[v]))

    if not visited[d]:
        print(-1)
        import sys

        sys.exit(0)

    cur = d
    path = []
    while cur != last[cur]:
        path.append(cur)
        cur = last[cur]

    path.append(s)
    print(dist[d])
    for p in reversed(path):
        print(p, end=" ")
