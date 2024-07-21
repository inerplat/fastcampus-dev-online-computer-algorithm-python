class Student:
    def __init__(self, age, height):
        self.age = age
        self.height = height

    def __lt__(self, other):
        if self.age == other.age:
            return self.height < other.height
        return self.age < other.age


def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = arr[start]
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= pivot:
            left += 1
        while right > start and arr[right] >= pivot:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)



if __name__ == "__main__":
    n = int(input())
    students = []
    for _ in range(n):
        age, height = map(int, input().split())
        students.append(Student(age, height))
