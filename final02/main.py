def calculate_max_value(numbers, add_count, mul_count):
    n = len(numbers)
    dp = [[[-1_000_000_000] * (mul_count + 1) for _ in range(add_count + 1)] for _ in range(n)]

    for a in range(add_count + 1):
        for m in range(mul_count + 1):
            dp[0][a][m] = numbers[0]

    for i in range(1, n):
        for a in range(add_count + 1):
            for m in range(mul_count + 1):
                if a > 0:
                    dp[i][a][m] = max(dp[i][a][m], dp[i - 1][a - 1][m] + numbers[i])
                if m > 0:
                    dp[i][a][m] = max(dp[i][a][m], dp[i - 1][a][m - 1] * numbers[i])
    return dp[n - 1][add_count][mul_count]

if __name__ == "__main__":
    n, add_count, mul_count = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(calculate_max_value(numbers, add_count, mul_count))
