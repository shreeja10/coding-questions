class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new=[]
        for i in nums:
            if i not in new:
                new.append(i)
        k=len(new)
        nums[:k]=new
        return k
