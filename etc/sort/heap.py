class Student:
    def __init__(self, age, height):
        self.age = age
        self.height = height

    def __lt__(self, other):
        if self.age == other.age:
            return self.height < other.height
        return self.age < other.age


class MinHeap:
    def __init__(self, data):
        self.data = [None] + data  # 1-based indexing
        self.size = len(data)
        for i in range(self.size // 2, 0, -1):
            self.make_heap(i)

    def make_heap(self, i):
        left = 2 * i
        right = 2 * i + 1
        target = i
        if left <= self.size and self.data[left] < self.data[target]:
            target = left
        if right <= self.size and self.data[right] < self.data[target]:
            target = right
        if target != i:
            self.swap(i, target)
            self.make_heap(target)

    def swap(self, i, target):
        self.data[i], self.data[target] = self.data[target], self.data[i]

    def delete(self):
        root = self.data[1]
        self.swap(1, self.size)
        self.size -= 1
        self.make_heap(1)
        return root


if __name__ == "__main__":
    n = int(input())
    students = []

    for _ in range(n):
        age, height = map(int, input().split())
        students.append(Student(age, height))

    min_heap = MinHeap(students)
    for _ in range(n):
        student = min_heap.delete()
        print(student.age, student.height)
