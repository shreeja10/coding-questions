class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2==0:
            return n
        elif n%2!=0:
            return n*2