class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # dp = [0] * (n + 1)
        
        # # Every stage I want to store the minimum cost that I can take by
        # # 1 and 2 steps

        # dp[0] = 0
        # dp[1] = 0

        # for i in range(2,n+1):
        #     dp[i] = min(dp[i-1], dp[i-2]+dp[i-3]

        #     )

        dp = [-1] * (len(cost)+3)
        dp[-1] = 0
        dp[-2] = 0
        dp[-3] = 0

        def f(i):
            # base case
            if i >= len(cost):
                return 0
            # we have already seen f(i+1) and f(i+2)
            elif (dp[i+1] != -1) and (dp[i+2] != -1):
                dp[i] = cost[i] + min(dp[i+1], dp[i+2])
            # we have seen one of them
            elif (dp[i+1] != -1) and (dp[i+2] == -1):
                dp[i] = cost[i] + min(dp[i+1], f(i+2))
            elif (dp[i+1] == -1) and (dp[i+2] != -1):
                dp[i] = cost[i] + min(f(i+1), dp[i+2])
            # recursive case
            else:
                dp[i] = cost[i] + min(f(i+1), f(i+2))
            return dp[i]
        
        f(0)
        return min(dp[0], dp[1])




