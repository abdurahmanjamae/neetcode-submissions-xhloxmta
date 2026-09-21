class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)  # Dictionary where each key stores a list of anagrams

        for word in strs:  # Go through each word in the input list
            key = ''.join(sorted(word))  # Sort letters to create the same key for anagrams
            groups[key].append(word)  # Add the original word to its anagram group

        return list(groups.values())  # Return all anagram groups as a list

# Time: O(n * k log k)
# n = number of words, k = average word length
# Space: O(n * k)
# Mental cue: sort each word -> same sorted key -> same anagram group