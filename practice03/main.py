def euclid(a, b):
    # base case
    if b == 0:
        return a
    # recursive case
    return euclid(b, a % b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    print(euclid(a, b))
