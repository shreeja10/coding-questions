class Solution(object):
    def maxProductPair(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        max_product=float('-inf')
        product=0
        new=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j] and nums[i]+nums[j]==target and nums[i]!=nums[j]:
                    product=nums[i]*nums[j]
                    if product>max_product:
                        max_product=product
                        new=[i,j]
        if new==[]:
            return [-1,-1]
        return new