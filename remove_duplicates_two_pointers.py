class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        read=0
        write=1
        for read in range(len(nums)):
            if nums[read]!=nums[write-1]:
                nums[write]=nums[read]
                write+=1
        return write