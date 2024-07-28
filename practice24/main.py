def search(pattern, text):
    m = len(pattern)
    n = len(text)
    f = failure(pattern)

    i = 0
    j = 0
    count = 0

    while i < n:
        if pattern[j] == text[i]:
            j += 1
            i += 1

        if j == m:
            count += 1
            j = f[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = f[j - 1]
            else:
                i += 1

    return count


def failure(pattern):
    m = len(pattern)
    f = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            f[i] = length
            i += 1
        else:
            if length != 0:
                length = f[length - 1]
            else:
                f[i] = 0
                i += 1

    return f


if __name__ == "__main__":
    pattern = input().strip()
    text = input().strip()

    count = search(pattern, text)
    print(count)
