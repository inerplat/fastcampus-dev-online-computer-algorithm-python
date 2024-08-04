class Graph:
    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost


if __name__ == "__main__":
    v, e = map(int, input().split())
    adjList = [[] for _ in range(v + 1)]

    for _ in range(e):
        src, dest, cost = map(int, input().split())
        adjList[src].append(Graph(dest, cost))
        adjList[dest].append(Graph(src, cost))

    q = int(input().strip())
    result = []

    for _ in range(q):
        src, dest = map(int, input().split())
        if src == dest:
            result.append(0)
            continue

        found = False
        minCost = 1_000_000_000
        for graph in adjList[src]:
            if graph.dest == dest:
                found = True
                if graph.cost < minCost:
                    minCost = graph.cost
        if found:
            result.append(minCost)
        else:
            result.append(-1)

    for result in result:
        print(result)
