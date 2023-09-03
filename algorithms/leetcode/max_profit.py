class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_i = 0
        max_j = 0
        profit = 0
        max_profit = 0

        while max_j < len(prices):
            profit = prices[max_j] - prices[min_i]
            if prices[max_j] < prices[min_i]:
                min_i = max_j
            else:
                max_profit = max(max_profit, profit)
            max_j += 1

        return max_profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
