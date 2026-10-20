class Solution(object):
    def minDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
        return count