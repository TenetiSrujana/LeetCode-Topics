''' 
# Brute Force
class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        for x in nums:
            count = 0
            for y in nums:
                if x == y:
                    count += 1
            if count > n // 2:
                return x
# Time Complexity: O(n²)
# Space Complexity: O(1) 
'''

# Optimal
class Solution:
    def majorityElement(self, nums):
        candidate = 0
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
            if x == candidate:
                count += 1
            else:
                count -= 1
        return candidate
# Time Complexity: O(n)
# Space Complexity: O(1)