class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest=nums[0]
        second_largest=float('-inf')
        third_largest=float('-inf')
        for i in range(len(nums)):
            if nums[i]>largest:
                largest=nums[i]
        for i in range(len(nums)):
            if nums[i]>second_largest and nums[i]!=largest:
                second_largest=nums[i]
        for i in range(len(nums)):
            if nums[i]>third_largest and nums[i]!=largest and nums[i]!=second_largest:
                third_largest=nums[i]
        if third_largest == float('-inf'):
            return largest

        return third_largest