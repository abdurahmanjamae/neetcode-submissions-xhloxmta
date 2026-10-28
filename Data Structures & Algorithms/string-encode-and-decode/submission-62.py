class Solution:

    def encode(self, strs: List[str]) -> str:
        # Initialize an empty string to store the encoded result
        res = ''

        # Loop through each word in the list
        for s in strs:
            # Get the word's length and convert it to a string
            # Add '#' as a separator, followed by the word itself
            # Format: [length] + [#] + [word]
            # Example: "apple" becomes "5#apple"
            res += str(len(s)) + "#" + s

        # Return the final encoded string
        return res

    def decode(self, s: str) -> List[str]:
        # Initialize an empty list and a pointer at index 0
        res, i = [], 0

        # Keep looping until we've processed the entire encoded string
        while i < len(s):
            j = i

            # Step 1: Find the '#' to know where the length number ends
            while s[j] != "#":
                j += 1

            # Step 2: Convert the text before '#' into an integer (word length)
            length = int(s[i:j])

            # Step 3: Extract the word using its length (starts right after '#')
            word = s[j+1 : j+1+length]

            # Add the decoded word to our result list
            res.append(word)

            # Step 4: Move the pointer to the start of the next encoded segment
            i = j+1+length

        # Return the list of decoded words
        return res


# Mental Cue:
# Encode: Get Length → Add '#' → Add Word → Repeat
# Decode: Find '#' → Read Length → Extract Word → Move Pointer → Repeat

# Time Complexity: O(n) for both encode and decode
# n = total number of characters processed
# Each character is processed a constant number of times.

# Space Complexity:
# Encode: O(n) → Stores the encoded string.
# Decode: O(n) → Stores the decoded strings in a list.