class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.child:
                current.child[ch] = TrieNode()
            current = current.child[ch]
        current.is_end = True

    def delete(self, word):
        self._delete(self.root, word, 0)

    def _delete(self, current, word, index):
        # base case
        # 문자열의 끝에 도달한 경우
        if index == len(word):
            if not current.is_end:
                return False
            current.is_end = False
            return len(current.child) == 0
        ch = word[index]
        node = current.child.get(ch)
        if node is None:
            return False
        should_delete = self._delete(node, word, index + 1)

        if should_delete and not node.is_end:
            del current.child[ch]
            return len(current.child) == 0
        return False

    def find_all_words(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)

        for ch, next_node in node.child.items():
            self.find_all_words(next_node, prefix + ch, results)

    def search_by_prefix(self, prefix):
        current = self.root
        for ch in prefix:
            current = current.child.get(ch)
            if current is None:
                return []
        results = []
        self.find_all_words(current, prefix, results)
        return results

    def search(self, word):
        current = self.root
        for ch in word:
            current = current.child.get(ch)
            if current is None:
                return False
        return current.is_end


if __name__ == "__main__":
    m = int(input().strip())
    trie = Trie()
    for _ in range(m):
        command, argument = map(str, input().strip().split())
        if command == "ADD":
            trie.insert(argument)
        elif command == "REMOVE":
            trie.delete(argument)
        elif command == "SEARCH":
            words = trie.search_by_prefix(argument)
            if not words:
                print("404 Not found")
            else:
                words.sort()
                for word in words:
                    print(word)
            print("---")
