class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        ans = 0

        i = 1
        while i * i <= x:
            ans = i
            i += 1

        return ans
