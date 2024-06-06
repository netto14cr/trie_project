from TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if not current.has_child(char):
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if not current.has_child(char):
                return False
            current = current.children[char]
        return current.is_end_of_word

    def delete(self, word):
        return self._delete(self.root, word, 0)

    def _delete(self, current, word, index):
        if index == len(word):
            if not current.is_end_of_word:
                return False
            current.is_end_of_word = False
            return len(current.children) == 0

        char = word[index]
        if not current.has_child(char):
            return False

        can_delete = self._delete(current.children[char], word, index + 1)
        if can_delete:
            del current.children[char]
            return len(current.children) == 0

        return False

    def get_words_with_prefix(self, prefix):
        current = self.root
        for char in prefix:
            if not current.has_child(char):
                return []
            current = current.children[char]
        return self._get_all_words_from_node(current, prefix)

    def _get_all_words_from_node(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            words.extend(self._get_all_words_from_node(next_node, prefix + char))
        return words
