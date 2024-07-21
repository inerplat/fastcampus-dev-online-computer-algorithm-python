def select_sort(arr):
    end = len(arr)
    for start in range(end):
        min_index = start
        for j in range(start + 1, end):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[start], arr[min_index] = arr[min_index], arr[start]


if __name__ == "__main__":
    arr = [2, 5, 8, 7, 3, 1]
    select_sort(arr)
    print(arr)
