class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)//2
        new={}
        for i in nums:
            if i not in new:
                new[i]=1
            elif i in new:
                new[i]+=1
        for keys,values in new.items():
            if values>n:
                return keys