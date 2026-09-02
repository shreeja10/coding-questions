class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 1

        if x < 0:
            n = -1
            x = x * -1

        rev = 0

        while x > 0:
            last = x % 10
            rev = rev * 10 + last
            x = x // 10
            if rev<-2**31 or rev>2**31-1:
                return 0
        return rev * n