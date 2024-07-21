if __name__ == "__main__":
    price = int(input())
    n = int(input())
    coin = [0] + list(map(int, input().split()))
    dp = [1_000_000_000] * (10000 * 2 + 10)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(0,  price + 1):
            dp[j + coin[i]] = min(dp[j + coin[i]], dp[j] + 1)

    # for i in range(1, n + 1):
    #     for j in range(coin[i], price + 1):
    #         dp[j] = min(dp[j], dp[j - coin[i]] + 1)

    if dp[price] == 1_000_000_000:
        print(-1)
    else:
        print(dp[price])