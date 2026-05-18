class PrefixTree:

    def __init__(self):
        # Initialize the root of the trie as an empty dictionary
        self.trie = {}
        

    def insert(self, word: str) -> None:
        # Start at the root dictionary
        d = self.trie

        # Traverse through each character in the word
        for c in word:
            # If the character doesn't exist, create a new nested dictionary
            if c not in d:
                d[c] = {}
            # Move deeper into the trie
            d = d[c]
        # Mark the end of a valid word using a special terminal key
        d['.'] = '.'


    def search(self, word: str) -> bool:
        # Start at the root dictionary
        d = self.trie
        
        # Traverse through each character in the word
        for c in word:
            # If a character is missing, the word does not exist
            if c not in d:
                return False
            # Move deeper into the trie
            d = d[c]
        # Return True only if the terminal key exists at this node
        return '.' in d
        

    def startsWith(self, prefix: str) -> bool:
        # Start at the root dictionary
        d = self.trie
        
        # Traverse through each character in the prefix
        for c in prefix:
            # If a character is missing, the prefix does not exist
            if c not in d:
                return False
            # Move deeper into the trie
            d = d[c]
        # If all characters are found, the prefix exists in the trie
        return True


# Complexity Analysis:
# Let L be the length of the string (word or prefix) being processed, 
# and let N be the total number of words inserted into the Trie.
#
# Time Complexity:
#   - insert(word):    O(L) -> Must iterate through every character of the word.
#   - search(word):    O(L) -> Traverses at most L nodes to find the word.
#   - startsWith(pre): O(L) -> Traverses at most L nodes to match the prefix.
#
# Space Complexity:
#   - O(N * L) worst-case -> In the absolute worst scenario where no words share 
#     any common prefixes, every single character of every word requires its own 
#     separate dictionary node.