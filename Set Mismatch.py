class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        new=[]
        nums_set=set(nums)
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for keys,values in d.items():
            if values==2:
                new.append(keys)
        for i in range(1,len(nums)+1):
            if i not in nums:
                new.append(i)
        return new