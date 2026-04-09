class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary mapping sorted word -> list of anagrams
        groups = defaultdict(list)

        # Process each word
        for word in strs:
            # Sort characters in the word to form a common key
            key = ''.join(sorted(word))

            # Add the word to its anagram group
            groups[key].append(word)

        # Return all grouped anagrams
        return list(groups.values())