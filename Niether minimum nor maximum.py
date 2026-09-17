class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = min(nums)
        b = max(nums)
        for i in nums:
            if i != a and i != b:
                return i

        return -1