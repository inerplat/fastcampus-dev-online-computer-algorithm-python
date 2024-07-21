cache = [0] * 1001


def hanoi(n):
    # memoization
    if cache[n] != 0:
        return cache[n]
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursive case
    cache[n] = 2 * hanoi(n - 1) + 1
    return cache[n]


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(hanoi(n) - hanoi(k) + hanoi(k - 1))
