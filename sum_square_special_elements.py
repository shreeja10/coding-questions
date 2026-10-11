class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for i in range(1,len(nums)+1):
            if len(nums)%i==0:
                total+=nums[i-1]*nums[i-1]
        return total