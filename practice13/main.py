class Graph:
    def __init__(self, dest, time):
        self.dest = dest
        self.time = time

    def __lt__(self, other):
        return self.time < other.time

import queue

if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        s, d, c = map(int, input().split())
        graph[s].append(Graph(d, c))

    start, end = map(int, input().split())

    dist = [1_000_000_000] * (v + 1)
    visited = [False] * (v + 1)
    last = [0] * (v + 1)

    pq = queue.PriorityQueue()
    pq.put(Graph(start, 0))
    dist[start] = 0
    last[start] = start

    while pq.qsize() > 0:
        cur = pq.get()
        u = cur.dest
        if visited[u]:
            continue
        visited[u] = True
        for g in graph[u]:
            nxt = g.dest
            if dist[nxt] > dist[u] + g.time:
                dist[nxt] = dist[u] + g.time
                last[nxt] = u
                pq.put(Graph(nxt, dist[nxt]))

    if not visited[end]:
        print(-1)
        import sys
        sys.exit(0)

    cur = end
    path = []
    while cur != last[cur]:
        path.append(cur)
        cur = last[cur]

    path.append(start)

    print(dist[end])
    for p in reversed(path):
        print(p, end=" ")

