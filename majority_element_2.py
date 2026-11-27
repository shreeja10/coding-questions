class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        d={}
        new=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for keys,values in d.items():
            if values>n/3:
                new.append(keys)
        return new