class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest=nums[0]
        largest_index=0
        for i in range(len(nums)):
            if nums[i]>largest:
                largest=nums[i]
                largest_index=i
        for i in range(len(nums)):
            if nums[i]!=largest:
                if nums[i]*2>largest:
                    return -1
        return largest_index