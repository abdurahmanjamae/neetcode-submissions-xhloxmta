class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" # start w/ the string
        for s in strs:
            res += str(len(s)) + "*" + s # add l + separator + s itself
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s): # keep looping as long as i hasn't reached end of s
            j = i
            while s[j] != "*": #move j forward until separtor is found
                j += 1
            
            length = int(s[i:j]) #convert that substring, we now know how many chars belong to the next word

            word = s[j+1 : j+1+length] # start right after the *, append and find the encoded part
            res.append(word)
            i = j + 1 + length #this will set i to the begin, ready for next loop
        return res
