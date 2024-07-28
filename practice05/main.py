import sys


def radix_sort(arr, n):
    max_num = max(arr)
    exp = 1
    bucket = [[] for _ in range(10)]

    while max_num >= exp:
        for i in range(n):
            digit = (arr[i] // exp) % 10
            bucket[digit].append(arr[i])

        index = 0
        for i in range(10):
            for j in range(len(bucket[i])):
                arr[index] = bucket[i][j]
                index += 1
            bucket[i].clear()

        exp *= 10


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    radix_sort(arr, n)

    sys.stdout.write(" ".join(map(str, arr)) + " \n")