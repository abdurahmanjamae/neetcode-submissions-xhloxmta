class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # Dictionary where each key stores a list of anagrams

        for word in strs:  # Go through each word in the input list
            key = ''.join(sorted(word))  # Sort letters to create the same key for anagrams
            groups[key].append(word)  # Add the original word to its anagram group

        return list(groups.values())  # Return all anagram groups as a list

# Time: O(n * m log m) Loop through n words and sort each word in O(m log m).
# n = number of words, m = average word length
# Space: O(n * m) Store n words, each averaging m characters.
# Mental cue: sort each word -> same sorted key -> same anagram group