class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        temp = set()
        result = []
        for p1 in range(len(nums)):
            p2 = p1 + 1
            p3 = len(nums) - 1
            while p2 < p3:
                total = sortedNums[p1] + sortedNums[p2] + sortedNums[p3]

                if total < 0:
                    p2 += 1
                elif total > 0:
                    p3 -= 1
                else:
                    temp.add((sortedNums[p1],
                    sortedNums[p2],
                    sortedNums[p3]))
                    p2 += 1
                    p3 -= 1
        return [list(elem) for elem in temp]

