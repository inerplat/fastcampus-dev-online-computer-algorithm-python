class Fish:
    def __init__(self, cost, weight):
        self.cost = cost
        self.weight = weight


if __name__ == "__main__":
    n, m = map(int, input().split())
    fish = [Fish(0, 0)]
    for i in range(n):
        weight, cost = map(int, input().split())
        fish.append(Fish(cost, weight))

    # dp = [[0] * (m + 1) for _ in range(n + 1)]
    # for i in range(1, n + 1):
    #     for w in range(1, m + 1):
    #         if w - fish[i].weight < 0:
    #             dp[i][w] = dp[i - 1][w]
    #         else:
    #             dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - fish[i].weight] + fish[i].cost)
    # print(dp[n][m])

    dp = [0] * (m + 1)
    prev = [0] * (m + 1)
    for i in range(1, n + 1):
        for w in range(1, m + 1):
            if w - fish[i].weight < 0:
                dp[w] = prev[w]
            else:
                dp[w] = max(prev[w], prev[w - fish[i].weight] + fish[i].cost)

        for j in range(1, m + 1):
            prev[j] = dp[j]
            dp[j] = 0

    print(prev[m])
