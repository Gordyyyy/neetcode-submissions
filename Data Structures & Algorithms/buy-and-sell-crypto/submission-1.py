class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 99999
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            
            profit = price - minPrice

            if profit > maxProfit:
                maxProfit = profit
            
        return maxProfit



        # d = {}
        # # key: Buy Price
        # # value: Highest sell price

        # for i in range(len(prices)-1):
        #     currentPrice = prices[i]
        #     rest = prices[i+1:]
        #     bestSell = max(rest)
        #     bestProfit = bestSell - currentPrice
        #     if bestProfit < 0:
        #         bestProfit = 0
        #     d[currentPrice] = bestProfit
        # # Now we have the dictionary filled with: price : largest Profit
        # bestResult = 0
        # for value in d.values():
        #     if value > bestResult:
        #         bestResult = value
        # return bestResult



        
        