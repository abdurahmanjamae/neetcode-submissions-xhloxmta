class WordDictionary:

    def __init__(self):
        # Initialize the root of the trie as an empty dictionary
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        # Start at the root dictionary
        d = self.trie
        
        # Traverse through each character in the word
        for c in word:
            # If the character node doesn't exist, create it
            if c not in d:
                d[c] = {}
            # Move down to the next character's dictionary
            d = d[c]
        # Mark the end of a valid word using a list terminal marker
        d["$"] = ["$"]
        

    def search(self, word: str) -> bool:
        # Helper function to perform Depth-First Search matching
        def dfs(index, current_dict):
            d = current_dict

            # Iterate through the characters starting from the current index
            for i in range(index, len(word)):
                c = word[i]
                
                # If a wildcard dot is encountered, initiate backtracking
                if c == '.':
                    # Check every possible character path available at this node
                    for key in d:
                        # Skip the end-of-word marker and recursively search the remaining string
                        if key != "$" and dfs(i+1, d[key]):
                            return True
                    # If no paths match the remaining string, backtrack
                    return False
                else:
                    # Standard matching: if the exact character is missing, search fails
                    if c not in d:
                        return False
                    # Move deeper into the character path
                    d = d[c]
            # Check if we landed on a valid end-of-word marker
            return "$" in d
            
        # Begin the recursive evaluation from index 0 and the root dictionary
        return dfs(0, self.trie)


# Complexity Analysis:
# Let L be the maximum length of a word being processed, 
# let N be the total number of words inserted into the data structure, 
# and let M be the total number of unique character nodes present within the Trie.
#
# Time Complexity:
#   - addWord(word): O(L) 
#     Requires iterating through and processing exactly every character of the string.
#
#   - search(word):  O(M) worst-case, O(L) best-case
#     If the search query contains no wildcards ('.'), it runs in O(L) time by following a 
#     single deterministic path. However, in the worst-case scenario with heavy wildcard patterns 
#     (e.g., searching for "...." in a densely populated trie), the DFS traversal might have 
#     to visit every single node in the entire structure, resulting in O(M).
#
# Space Complexity:
#   - addWord(word): O(N * L) worst-case 
#     In the absolute worst scenario where none of the inserted words share common prefixes, 
#     every single character requires its own dedicated nested dictionary node.
#
#   - search(word):  O(L) auxiliary space 
#     The recursive depth-first search helper function consumes memory on the execution call stack, 
#     which will reach a maximum depth directly proportional to the length of the string L.