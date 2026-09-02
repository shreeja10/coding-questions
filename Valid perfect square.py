class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ans = 0
        i = 1
        while i * i <= num:
            if i * i == num:
                ans = i
                return True
            i += 1
        return False
