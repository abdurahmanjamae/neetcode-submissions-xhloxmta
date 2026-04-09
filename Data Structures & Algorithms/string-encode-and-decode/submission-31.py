class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            # Format: [length of word] + [# separator] + [the word itself]
            # Example: "apple" becomes "5#apple"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            # Step 1: Find the '#' to know where the length number ends
            while s[j] != "#":
                j += 1

            # Step 2: Convert the text before '#' into an integer (the word length)
            length = int(s[i:j])
            
            # Step 3: Extract the word using the length (starts right after '#')
            word = s[j+1 : j+1+length]
            res.append(word)
            
            # Step 4: Move the pointer to the start of the next encoded segment
            i = j+1+length
            
        return res