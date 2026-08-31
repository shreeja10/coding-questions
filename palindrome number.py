class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n=0
        rev=0
        last=0
        original=x
        if x<0:
            n=-1
            x=n*x
        while x>0:
            last=x%10
            rev=rev*10+last
            x=x//10
        if x<0:
            x=n*x
        if original==rev:
            return True
        else:
            return False
