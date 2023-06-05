# https://leetcode.com/problems/implement-trie-prefix-tree/


# TODO: This works, but needs optimization
# TODO: See if we can create a SVG from this - idea from https://twitch.tv/tsoding


class Node:
    """Represents the node in the Trie"""

    def __init__(self, letter=None, children=None, is_word=False):
        self.letter = letter
        if children is None:
            self.children = set()
        else:
            self.children = set(children)
        self.is_word = is_word


class Trie:
    """Represents a Prefix tree/Trie"""

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """Insert a word in the Trie

        :param word: The word to insert
        """
        if len(word) == 0:
            return
        curr = self.root
        for letter in word:
            letters = set(map(lambda n: n.letter, curr.children))
            if letter in letters:
                for n in curr.children:
                    if n.letter == letter:
                        curr = n
            else:
                node = Node(letter)
                curr.children.add(node)
                curr = node
        curr.is_word = True

    def search(self, word: str) -> bool:
        """Searches if the word is present in the Trie

        :param word: The word to search
        :returns: If the word is present in the Trie
        :rtype: bool
        """
        if len(word) == 0:
            return False

        curr = self.root
        found = True
        for letter in word:
            letters = set(map(lambda n: n.letter, curr.children))
            if letter in letters:
                for n in curr.children:
                    if n.letter == letter:
                        curr = n
            else:
                found = False
                break

        if found:
            found = curr.is_word

        return found

    def startsWith(self, prefix: str) -> bool:
        """startsWith returns true if there are any words which startwith the
        given prefix

        :param prefix: The prefix for which we need to find any words/s starts with
        :returns: True if word starts with the given prefix
        :rtype: bool
        """
        if len(prefix) == 0:
            # If we have some nodes in the tree under ROOT, "" is a prefix for all words
            return len(self.root) != 0

        curr = self.root
        starts_with = True
        for letter in prefix:
            letters = set(map(lambda n: n.letter, curr.children))
            if letter in letters:
                for n in curr.children:
                    if n.letter == letter:
                        curr = n
            else:
                starts_with = False
                break

        return starts_with


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
