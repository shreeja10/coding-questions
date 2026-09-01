class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new={}
        for i in nums:
            if i%2==0 and i not in new:
                new[i]=1
            elif i%2==0 and i in new:
                new[i]+=1
        for i in nums:
            if i % 2 == 0 and new[i] == 1:
                return i

        return -1