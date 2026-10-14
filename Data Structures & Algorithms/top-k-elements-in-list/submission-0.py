class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            d[num] = d.get(num,0) + 1
        # Now our dictionary has all the number: # of occurance 

        temp = []
        for num,numOccurance in d.items():
            temp.append((numOccurance,num))
        sortedTemp = sorted(temp,reverse = True)
        result = []
        for time in range(k):
            result.append(sortedTemp[time][1])
        return result