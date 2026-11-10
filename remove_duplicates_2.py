class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        read=0
        write=2
        if len(nums)<=2:
            return len(nums)
        for read in range(2,len(nums)):
            if nums[read]!=nums[write-2]:
                nums[write]=nums[read]
                write+=1
        return write