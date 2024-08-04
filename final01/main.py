from queue import PriorityQueue

class Graph:
    def __init__(self, dest, time):
        self.dest = dest
        self.time = time

    def __lt__(self, other):
        return self.time < other.time

def dijkstra(v, e, start, end, edges):
    graph = [[] for _ in range(v + 1)]
    for s, d, c in edges:
        graph[s].append(Graph(d, c))
        graph[d].append(Graph(s, c))

    dist = [float('inf')] * (v + 1)
    visited = [False] * (v + 1)
    pq = PriorityQueue()
    pq.put(Graph(start, 0))

    dist[start] = 0
    while not pq.empty():
        cur = pq.get()
        current = cur.dest
        if visited[current]:
            continue
        visited[current] = True
        for g in graph[current]:
            next = g.dest
            if dist[next] > dist[current] + g.time:
                dist[next] = dist[current] + g.time
                pq.put(Graph(next, dist[next]))

    if not visited[end]:
        return -1
    return dist[end]

if __name__ == "__main__":
    v, e, start, end = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(e)]
    result = dijkstra(v, e, start, end, edges)
    print(result)
