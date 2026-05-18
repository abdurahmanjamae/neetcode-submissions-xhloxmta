class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d["$"] = ["$"]
        

    def search(self, word: str) -> bool:
        def dfs(index, current_dict):
            d = current_dict

            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    for key in d:
                        if key != "$" and dfs(i+1, d[key]):
                            return True
                    return False
                else:
                    if c not in d:
                        return False
                    d = d[c]
            return "$" in d
        return dfs(0, self.trie)
        
