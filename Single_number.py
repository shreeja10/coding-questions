class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new={}
        for i in nums:
            if i not in new:
                new[i]=1
            elif i in new:
                new[i]+=1
        for keys,values in new.items():
            if values==1:
                return(keys)