''' 
# Brute Force:
class Solution:
    def removeElement(self, nums, val):
        result = []
        for x in nums:
            if x != val:
                result.append(x)
        for i in range(len(result)):
            nums[i] = result[i]
        return len(result)

Time: O(n)
Space: O(n) '''

# optimal :
class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# Time: O(n)
# Space: O(1)