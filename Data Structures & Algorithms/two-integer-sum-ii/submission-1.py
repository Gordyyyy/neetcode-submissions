class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            rest = target - numbers[left]
            if numbers[right] > rest:
                right -= 1
            elif numbers[right] == rest:
                return [left+1,right+1]
            elif numbers[right] < rest:
                left += 1
                continue
        return None