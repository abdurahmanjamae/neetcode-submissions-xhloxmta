class Solution:

    def encode(self, strs: List[str]) -> str:
        # Result string that will store the encoded version
        res = ''

        # Go through each word in the list
        for s in strs:
            # Add: length of word + '#' + the word itself
            # Example: "hello" → "5#hello"
            res += str(len(s)) + "#" + s

        # Return the final encoded string
        return res

    def decode(self, s: str) -> List[str]:
        # List to store decoded words
        # i is a pointer used to walk through the string
        res, i = [], 0

        # Loop until we reach the end of the string
        while i < len(s):
            # j will move forward to find the '#'
            j = i

            # Move j until we find the delimiter '#'
            while s[j] != "#":
                j += 1

            # Convert the substring before '#' into the word length
            length = int(s[i:j])

            # Extract the word using the known length
            word = s[j + 1 : j + 1 + length]

            # Add the decoded word to the result list
            res.append(word)

            # Move i to the start of the next encoded word
            i = j + 1 + length

        # Return the list of decoded words
        return res

