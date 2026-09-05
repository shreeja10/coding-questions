class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing=[]
        nums_set=set(nums)
        for i in range(1,len(nums)+1):
           if i not in nums_set:
            missing.append(i)
        return missing