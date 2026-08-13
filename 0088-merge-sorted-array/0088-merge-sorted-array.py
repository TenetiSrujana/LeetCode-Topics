'''# Brute Force
class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()

Time: O((m+n) log(m+n))
Space: O(1)'''

# Optimal
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
# Time: O(m+n) ✅
# Space: O(1) ✅