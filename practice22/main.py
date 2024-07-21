if __name__ == "__main__":
    s1 = input()
    s2 = input()
    n = len(s1)
    m = len(s2)
    s1 = " " + s1
    s2 = " " + s2
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    print(dp[n][m])
