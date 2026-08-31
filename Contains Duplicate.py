class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new={}
        for i in nums:
            if i not in new:
                new[i]=1
            else:
                new[i]+=1
        for keys,values in new.items():
            if values>1:
                return True
        return False