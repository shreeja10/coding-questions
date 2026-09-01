class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        square=[]
        for i in range(len(nums)):
            square.append(nums[i]*nums[i])
            square.sort()
        return square