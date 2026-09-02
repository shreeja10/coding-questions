class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last=0
        for i in range(len(nums)):
            rev=0
            num=nums[i]
            while num>0:
                last=num%10
                rev=rev*10+last
                num=num//10
            nums.append(rev)
        nums_set=set(nums)
        return(len(nums_set))