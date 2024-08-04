class SubstringHash:
    def __init__(self, hash_value, string):
        self.hash = hash_value
        self.string = string

    def __lt__(self, other):
        return self.hash < other.hash

D = 257
M = (2**63) - 1 // D

def divide(s):
    left, right = 1, len(s)
    while left <= right:
        mid = (left + right) // 2
        if search(s, mid):
            left = mid + 1
        else:
            right = mid - 1
    return right

def search(s, length):
    hashes = []
    current_hash = hash_value(s, length)
    baseL = 1

    for i in range(length - 1):
        baseL = (baseL * D) % M

    hashes.append(SubstringHash(current_hash, s[:length]))

    for i in range(length, len(s)):
        current_hash = (current_hash - ord(s[i - length]) * baseL) % M
        if current_hash < 0:
            current_hash += M
        current_hash = (current_hash * D + ord(s[i])) % M
        hashes.append(SubstringHash(current_hash, s[i - length + 1:i + 1]))

    hashes.sort()
    for i in range(1, len(hashes)):
        if hashes[i].hash == hashes[i - 1].hash and hashes[i].string == hashes[i - 1].string:
            return True
    return False

def hash_value(s, length):
    h = 0
    for i in range(length):
        h = (h * D + ord(s[i])) % M
    return h

if __name__ == "__main__":
    s = input().strip()
    print(divide(s))
