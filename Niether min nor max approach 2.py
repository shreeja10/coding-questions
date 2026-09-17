class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        b = nums[0]
        for i in range(len(nums)):
            if nums[i] > a:
                a = nums[i]
        for i in range(len(nums)):
            if nums[i] < b:
                b = nums[i]
        for i in nums:
            if i != a and i != b:
                return i

        return -1