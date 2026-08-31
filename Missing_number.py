class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        actual_sum=0
        missing_number=0
        total=(len(nums)*(len(nums)+1))//2
        for i in nums:
            actual_sum+=i
        missing_number=total-actual_sum
        return(missing_number)