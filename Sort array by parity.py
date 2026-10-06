class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in nums:
            if i%2==0:
                new.append(i)
        for i in nums:
            if i%2!=0:
                new.append(i)
        return new