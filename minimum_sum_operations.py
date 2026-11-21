class Solution(object):
    def minRange(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        original=max(a,b,c)-min(a,b,c)
        d=max(b+c,b,c)-min(b+c,b,c)
        e=max(a,a+c,c)-min(a,a+c,c)
        f=max(a,b,a+b)-min(a,b,a+b)
        return(min(original,d,e,f))©leetcode