class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        result = []
        # Key: sorted word
        # Value: list of all the 
        for word in strs:
            sortedWord = tuple(sorted(word))
            if sortedWord not in d:
                d[sortedWord] = []
                d[sortedWord].append(word)
            else:
                d[sortedWord].append(word)
        
        for value in d.values():
            result.append(value)
        return result

        
        
        