def search(arr, start, end, key):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= key:
            end = mid
        else:
            start = mid + 1
    return end


if __name__ == "__main__":
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    # lis = [1] * n
    #
    # for i in range(1, n):
    #     for j in range(i):
    #         if arr[i] > arr[j]:
    #             lis[i] = max(lis[i], lis[j] + 1)
    d = [0] * (n + 1)
    d[1] = arr[1]
    idx = 1
    for i in range(2, n + 1):
        if arr[i] > d[idx]:
            idx += 1
            d[idx] = arr[i]
        else:
            pos = search(d, 1, idx, arr[i])
            d[pos] = arr[i]

    print(idx)
