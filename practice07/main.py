import queue


def isSafe(x, y, n):
    return 1 <= x <= n and 1 <= y <= n


def bfs(maze, n):
    if maze[1][1] == 1 or maze[n][n] == 1:
        return "SAD"

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = queue.Queue()
    q.put((1, 1))
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    visited[1][1] = True

    while not q.empty():
        x, y = q.get()

        if x == n and y == n:
            return "HAPPY"

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if isSafe(nx, ny, n) and not visited[nx][ny] and maze[nx][ny] == 0:
                q.put((nx, ny))
                visited[nx][ny] = True

    return "SAD"


def dfs(maze, n):
    if maze[1][1] == 1 or maze[n][n] == 1:
        return "SAD"

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(1, 1)]
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    visited[1][1] = True

    while stack:
        x, y = stack.pop()

        if x == n and y == n:
            return "HAPPY"

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if isSafe(nx, ny, n) and not visited[nx][ny] and maze[nx][ny] == 0:
                stack.append((nx, ny))
                visited[nx][ny] = True

    return "SAD"


if __name__ == "__main__":
    n = int(input())
    maze = [0]
    for _ in range(n):
        maze.append([0] + list(map(int, input().split())))

    print(dfs(maze, n))
