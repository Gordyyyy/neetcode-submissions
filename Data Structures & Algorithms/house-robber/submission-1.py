class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums)+3)
        dp[-1] = 0 
        dp[-2] = 0
        dp[-3] = 0

        def f(i):
            # base
            if i >= len(nums):
                return 0
            # shortcut for calculation
            elif (dp[i+2] != -1) and (dp[i+3] != -1):
                dp[i] = nums[i] + max(dp[i+2],dp[i+3])
            elif (dp[i+2] != -1) and (dp[i+3] == -1):
                dp[i] = nums[i] + max(dp[i+2],f(i+3))
            elif (dp[i+2] == -1) and (dp[i+3] != -1):
                dp[i] = nums[i] + max(f(i+2),dp[i+3])

            # Real recursive part
            else:
                # Updates to my global variable
                dp[i] = nums[i] + max(f(i+2),f(i+3))
            return dp[i]
        # Plug in the dp.
        f(0)
        f(1)
        result = max(dp[0],dp[1])
        return result


