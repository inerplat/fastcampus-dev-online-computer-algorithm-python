import queue


def bfs(graph, x):
    q = queue.Queue()
    chk[x] = True
    q.put(x)
    while not q.empty():
        v = q.get()
        for des in graph[v]:
            if not chk[des]:
                chk[des] = True
                q.put(des)


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    chk = [False] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    cnt = 0
    for i in range(1, n + 1):
        if not chk[i]:
            bfs(graph, i)
            cnt += 1
    print(cnt - 1)
