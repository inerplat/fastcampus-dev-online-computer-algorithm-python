D = 256
M = 2 ** 31 - 1


def rabin_karp(pattern, text):
    m = len(pattern)
    n = len(text)
    pattern_hash = hash(pattern, m)
    text_hash = hash(text, m)
    count = 0

    if pattern_hash == text_hash and check_equality(text, pattern, 0):
        count += 1

    base_power = 1
    for i in range(1, m):
        base_power = (base_power * D) % M



    for i in range(1, n - m + 1):
        text_hash = (text_hash - ord(text[i - 1]) * base_power) % M
        text_hash = text_hash * D % M
        text_hash = text_hash + ord(text[i + m - 1]) % M
        if pattern_hash == text_hash and check_equality(text, pattern, i):
            count += 1

    return count


def hash(string, length):
    hash_value = 0
    for i in range(length):
        hash_value = (hash_value * D + ord(string[i])) % M
    return hash_value


def check_equality(text, pattern, start):
    for i in range(len(pattern)):
        if text[start + i] != pattern[i]:
            return False
    return True


if __name__ == "__main__":
    pattern = input().strip()
    text = input().strip()

    print(rabin_karp(pattern, text))
