if __name__ == "__main__":
    n, m = map(int, input().split())
    dist = [[1_000_000_000] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    for _ in range(m):
        src, dest, cost = map(int, input().split())
        dist[src][dest] = min(dist[src][dest], cost)
        dist[dest][src] = min(dist[dest][src], cost)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] == 1_000_000_000:
                print("INF ", end="")
            else:
                print(dist[i][j], end=" ")
        print()
