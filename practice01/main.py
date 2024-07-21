def fibo(x):
    # base case
    if x == 0:
        return 0
    elif x == 1:
        return 1

    # recursive case
    if x > 1:
        return fibo(x - 1) + fibo(x - 2)
    elif x < 0:
        return fibo(x + 2) - fibo(x + 1)


if __name__ == "__main__":
    n = input()
    print(fibo(int(n)))
