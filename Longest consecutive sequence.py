class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        current=1
        longest=1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                current+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                current=1
            longest=max(longest,current)
        return longest