class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        d={}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for keys,values in d.items():
            if values==1:
                total+=keys
        return total