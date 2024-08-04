def divide(sales, n, x):
    left = 1
    right = n
    min_length = -1

    while left < right:
        mid = (left + right) // 2
        if decision(sales, n, mid, x):
            min_length = mid
            right = mid
        else:
            left = mid + 1

    return min_length != -1

def decision(sales, n, length, x):
    sum_sales = sum(sales[:length])
    if sum_sales / length >= x:
        return True

    for i in range(length, n):
        sum_sales += sales[i] - sales[i - length]
        if sum_sales / length >= x:
            return True

    return False

if __name__ == "__main__":
    n, x = map(int, input().split())
    sales = list(map(int, input().split()))

    can_aggro = divide(sales, n, x)
    if can_aggro:
        print("YES")
    else:
        print("NO")
