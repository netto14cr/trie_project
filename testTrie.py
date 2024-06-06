from Trie import Trie


def print_trie(trie, node=None, word='', words=None):
    if words is None:
        words = []

    if node is None:
        node = trie.root

    if node.is_end_of_word:
        words.append(word)

    for char, child_node in node.children.items():
        print_trie(trie, child_node, word + char, words)

    return words

def display_words_in_columns(words, columns=5):
    max_length = max(len(word) for word in words) + 2
    for i, word in enumerate(words):
        print(f"{word.ljust(max_length)}", end='')
        if (i + 1) % columns == 0:
            print()
    if len(words) % columns != 0:
        print()


def initialize_trie(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie

def delete_word(trie, word):
    if trie.search(word):
        trie.delete(word)
        print(f'Deleted "{word}" from dictionary\n')
    else:
        print(f'Did not find "{word}" in dictionary\n')

def get_spelling_suggestions(trie, word):
    suggestions = trie.get_words_with_prefix(word)
    if suggestions:
        print(f'Spelling suggestions for "{word}":')
        for suggestion in suggestions:
            print(suggestion)
    else:
        print(f'No suggestions found for "{word}".')

if __name__ == "__main__":
    words = [
        'as', 'astronaut', 'asteroid', 'are', 'around', 'cat', 'cars',
        'cares', 'careful', 'carefully', 'for', 'forgot', 'follows', 'from',
        'front', 'mellow', 'mean', 'money', 'monday', 'monster', 'place',
        'plan', 'planet', 'planets', 'plans', 'the', 'their', 'they',
        'there', 'towards'
    ]
    
    dictionary = initialize_trie(words)
    print("The dictionary contains the following words:")
    all_words = print_trie(dictionary)
    display_words_in_columns(all_words)

    while True:
        input_word = input("\nEnter a word to delete, or type 'suggest' to get suggestions, or press Enter to exit: ").strip()
        if not input_word:
            break
        if input_word.lower() == 'suggest':
            suggestion_word = input("Enter a word to get spelling suggestions for: ").strip()
            get_spelling_suggestions(dictionary, suggestion_word)
        else:
            delete_word(dictionary, input_word)
            print("The dictionary contains the following words:")
            all_words = print_trie(dictionary)
            display_words_in_columns(all_words)
