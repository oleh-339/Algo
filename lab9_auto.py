import os

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def autocomplete(self, prefix):
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
            
        results = []
        self._dfs(current, prefix, results)
        return results

    def _dfs(self, node, current_word, results):
        if node.is_end_of_word:
            results.append(current_word)
            
        for char, next_node in node.children.items():
            self._dfs(next_node, current_word + char, results)


def build_trie(patterns):
    trie = Trie()
    for word in patterns:
        trie.insert(word)
    return trie


if __name__ == "__main__":
    filename = "words.txt"

    with open(filename, "r", encoding="utf-8") as file:
        words_from_file = [line.strip().lower() for line in file if line.strip()]

    trie = build_trie(words_from_file)
    print("Щоб завершити, пишіть 'exit'\n")

    while True:
        user_input = input("Введіть префікс: ").strip().lower()
        
        if user_input == "exit":
            print("Кінець")
            break
            
        if not user_input:
            print("Пусто")
            continue

        found_words = trie.autocomplete(user_input)
        
        if found_words:
            print(f"Знайдені слова:")
            print(", ".join(found_words[:20]))
        else:
            print("Слів не знайдено")
