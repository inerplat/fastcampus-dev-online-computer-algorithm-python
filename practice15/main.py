import queue

if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    inDegree = [0] * (v + 1)
    for _ in range(e):
        src, dest = map(int, input().split())
        graph[src].append(dest)
        inDegree[dest] += 1

    q = queue.Queue()
    result = []

    for i in range(1, v + 1):
        if inDegree[i] == 0:
            q.put(i)
            result.append(i)

    while not q.empty():
        now = q.get()
        for next in graph[now]:
            inDegree[next] -= 1
            if inDegree[next] == 0:
                q.put(next)
                result.append(next)

    if len(result) != v:
        print("ERROR")
        import sys

        sys.exit(0)

    for x in result:
        print(x, end=" ")
