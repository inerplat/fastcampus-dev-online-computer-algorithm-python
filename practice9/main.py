if __name__ == "__main__":
    v, e = map(int, input().split())
    arr = [[float('inf')] * (v + 1) for _ in range(v + 1)]

    for _ in range(e):
        src, dest, cost = map(int, input().split())
        if arr[src][dest] > cost:
            arr[src][dest] = cost
        if arr[dest][src] > cost:
            arr[dest][src] = cost
    for i in range(v + 1):
        arr[i][i] = 0

    q = int(input())
    for _ in range(q):
        src, dest = map(int, input().split())
        if arr[src][dest] == float('inf'):
            print(-1)
        else:
            print(arr[src][dest])