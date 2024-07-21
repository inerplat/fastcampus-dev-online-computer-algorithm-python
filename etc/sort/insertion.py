def insertion_sort(arr):
    for i in range(1, len(arr)):
        target = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = target
    return arr


if __name__ == "__main__":
    arr = [2, 5, 8, 7, 3, 1]
    print(insertion_sort(arr))
