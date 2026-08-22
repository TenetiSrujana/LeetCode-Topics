'''
class Solution:
    def canJump(self, nums):
        def solve(i):
            if i >= len(nums) - 1:
                return True

            for jump in range(1, nums[i] + 1):
                if solve(i + jump):
                    return True

            return False

        return solve(0)

# Time Complexity: O(2^n)
# Space Complexity: O(n)
'''
#optimal
class Solution:
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

        return True

# Time Complexity: O(n)
# Space Complexity: O(1)