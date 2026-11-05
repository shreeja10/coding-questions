class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        el_sum=0
        digits_sum=0
        last=0
        for i in nums:
            el_sum+=i
        for i in nums:
            while i>0:
                last=i%10
                digits_sum+=last
                i=i//10
            else:
                digits_sum+=i
        return(abs(el_sum-digits_sum))