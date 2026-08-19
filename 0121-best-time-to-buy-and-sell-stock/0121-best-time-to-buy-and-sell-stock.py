'''# Brute Force
class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit
# Time Complexity: O(n²)
# Space Complexity: O(1)'''

# Optimal
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
# Time Complexity: O(n)
# Space Complexity: O(1)