from queue import PriorityQueue


class Graph:
    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, c = map(int, input().split())
        g[u].append(Graph(v, c))
        g[v].append(Graph(u, c))
    chk = [False] * (n + 1)
    ans = 0
    pq = PriorityQueue()
    pq.put(Graph(1, 0))
    while not pq.empty():
        cur = pq.get()
        dest = cur.dest
        cost = cur.cost
        if not chk[dest]:
            chk[dest] = True
            ans += cost
            for nxt in g[dest]:
                pq.put(nxt)

    if False in chk[1:]:
        print(-1)

    else:
        print(ans)
