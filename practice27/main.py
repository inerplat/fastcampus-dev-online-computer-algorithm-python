def main():
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    requirement = input().strip()

    cross_product = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

    if cross_product > 0:
        if requirement == "FAST":
            print(1)
        elif requirement == "SLOW":
            print(-1)
    elif cross_product < 0:
        if requirement == "FAST":
            print(-1)
        elif requirement == "SLOW":
            print(1)


if __name__ == "__main__":
    main()
