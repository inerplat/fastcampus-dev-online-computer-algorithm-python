class Graph:
    def __init__(self, dest, cost):
        self.dest = dest
        self.cost = cost


def main():
    v, e = map(int, input().split())

    adjList = [[] for _ in range(v + 1)]

    for _ in range(e):
        src, dest, cost = map(int, input().split())
        adjList[src].append(Graph(dest, cost))
        adjList[dest].append(Graph(src, cost))

    q = int(input().strip())

    results = []
    for _ in range(q):
        src, dest = map(int, input().split())

        if src == dest:
            results.append(0)
            continue

        found = False
        minCost = float('inf')

        for graph in adjList[src]:
            if graph.dest == dest:
                found = True
                if graph.cost < minCost:
                    minCost = graph.cost

        if found:
            results.append(minCost)
        else:
            results.append(-1)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
