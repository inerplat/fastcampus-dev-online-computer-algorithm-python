import queue

def isSafe(r, c, n):
    return 1 <= r <= n and 1 <= c <= n


def bfs(maze, n):
    if maze[1][1] == 1 or maze[n][n] == 1:
        return "SAD"
    q = queue.Queue()
    q.put((1, 1))
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    visited[1][1] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q.qsize() > 0:
        r, c = q.get()
        if r == n and c == n:
            return "HAPPY"

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if isSafe(nr, nc, n) and maze[nr][nc] == 0 and not visited[nr][nc]:
                q.put((nr, nc))
                visited[nr][nc] = True

    return "SAD"


if __name__ == "__main__":
    n = int(input())
    maze = [0]
    for _ in range(n):
        maze.append([0] + list(map(int, input().split())))

    answer = bfs(maze, n)
    print(answer)