'''
# brute force
class Solution:
    def maxProfit(self, prices):
        def solve(i, holding):
            if i == len(prices):
                return 0
            if holding:
                sell = prices[i] + solve(i + 1, False)
                skip = solve(i + 1, True)
                return max(sell, skip)
            else:
                buy = -prices[i] + solve(i + 1, True)
                skip = solve(i + 1, False)
                return max(buy, skip)
        return solve(0, False)
# Time Complexity: O(2^n)
# Space Complexity: O(n)  ← recursion stack
'''

class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
# Time Complexity: O(n)
# Space Complexity: O(1)