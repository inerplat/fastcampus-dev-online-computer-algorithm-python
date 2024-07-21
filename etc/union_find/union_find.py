def init(parent, n):
    for i in range(1, n + 1):
        parent[i] = i


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    x = find(a)
    y = find(b)
    parent[y] = x


if __name__ == "__main__":
    pass