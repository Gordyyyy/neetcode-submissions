class Solution:
    def rob(self, nums: List[int]) -> int:
        # Rob the first house
        dp = [-1] * (len(nums)+3) 
        dp[-1] = 0 
        dp[-2] = 0
        dp[-3] = 0
        arr1 = nums[0:len(nums)-1]
        # Don't rob the first house
        dp2 = [-1] * (len(nums)+3)
        dp2[-1] = 0
        dp2[-2] = 0
        dp2[-3] = 0
        arr2 = nums[1::]
        
        if len(nums) == 1:
            return nums[0]

        def f(i):
            # base case
            if i >= len(arr1):
                return 0
            # if we've seen the case
            elif dp[i+2] != -1 and dp[i+3] != -1:
                dp[i] = arr1[i] + max(dp[i+2],dp[i+3])
            elif dp[i+2] == -1 and dp[i+3] != -1:
                dp[i] = arr1[i] + max(f(i+2),dp[i+3])
            elif dp[i+2] != -1 and dp[i+3] != -1:
                dp[i] = arr1[i] + max(dp[i+2],f(i+3))
            # recursive case:
            else:
                dp[i] = arr1[i] + max(f(i+2),f(i+3))
            return dp[i]
        
        def f2(i):
            # base case
            if i >= len(arr2):
                return 0
            elif dp2[i+2] != -1 and dp2[i+3] != -1:
                dp2[i] = arr2[i] + max(dp2[i+2],dp2[i+3])
            elif dp2[i+2] == -1 and dp2[i+3] != -1:
                dp2[i] = arr2[i] + max(f2(i+2),dp2[i+3])
            elif dp2[i+2] != -1 and dp2[i+3] == -1:
                dp2[i] = arr2[i] + max(dp2[i+2],f2(i+3))
            # recursive case:
            else:
                dp2[i] = arr2[i] + max(f2(i+2),f2(i+3))
            return dp2[i]

        f(0)
        f(1)
        f2(0)
        f2(1)
        result = max(dp[0],dp[1],dp2[0],dp2[1])
        return result




