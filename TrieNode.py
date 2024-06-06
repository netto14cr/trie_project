class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def has_child(self, char):
        return char in self.children
