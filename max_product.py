class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        for i in range(len(nums)):
            a=nums[i]-1
            for j in range(i+1,len(nums)):
                if (a*(nums[j]-1))>m:
                    m=a*(nums[j]-1)
        return m