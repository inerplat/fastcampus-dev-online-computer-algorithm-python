if __name__ == "__main__":
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    require = input().strip()

    cross_product = x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)
    if cross_product > 0:
        if require == "FAST":
            print(1)
        elif require == "SLOW":
            print(-1)
    if cross_product < 0:
        if require == "FAST":
            print(-1)
        elif require == "SLOW":
            print(1)
