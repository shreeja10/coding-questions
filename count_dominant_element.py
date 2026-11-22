class Solution(object):
    def countDominantElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 1
        a=0
        count=0
        for i in range(1,len(nums)-1):
            a=(nums[i-1]+nums[i+1])/2.0
            if nums[i]>=a:
                count+=1
        if nums[0]>=nums[1] and nums[-1]>=nums[-2]:
            count+=2
        elif nums[0]>=nums[1] or nums[-1]>=nums[-2]:
            count+=1
        return count©leetcode