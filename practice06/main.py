import sys


def decision(daily, n, m, days):
    total = sum(daily[:days])
    if total >= m:
        return True
    for i in range(days, n):
        total += daily[i] - daily[i - days]
        if total >= m:
            return True
    return False


def search(n, m, daily):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if decision(daily, n, m, mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    daily = list(map(int, input().split()))

    print(search(n, m, daily))
