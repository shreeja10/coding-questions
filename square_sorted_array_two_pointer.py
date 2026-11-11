class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        new = []
        while left <= right:
            new.append(nums[left] ** 2)
            left += 1

        new.sort()
        return new