class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = max(nums)
        b = min(nums)
        new = []
        for i in range(1, b + 1):
            if a % i == 0 and b % i == 0:
                new.append(i)
                c = max(new)
        return c
