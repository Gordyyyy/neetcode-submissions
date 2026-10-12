class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for char in s:
            d1[char] = d1.get(char,0) + 1
        # Now my d1 has [Num:num of appearance]
        for char2 in t:
            d2[char2] = d2.get(char2,0) + 1
        # Now my e2 has num:numappearance
        return d1 == d2

        
        