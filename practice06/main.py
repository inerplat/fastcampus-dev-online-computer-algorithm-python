def decision(daily, n, m, days):
    total = sum(daily[:days])
    if total >= m:
        return True
    for i in range(days, n):
        total += daily[i] - daily[i - days]
        if total >= m:
            return True
    return False


def search(daily, n, m, start, end):
    if start >= end:
        return start
    mid = (start + end) // 2
    if decision(daily, n, m, mid):
        return search(daily, n, m, start, mid)
    else:
        return search(daily, n, m, mid + 1, end)


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    daily = list(map(int, input().split()))
    print(search(daily, n, m, 1, n))
