class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left=0
        right=int(c ** 0.5)
        while left<=right:
            total=left**2+right**2
            if (total)==c:
                return True
            elif (total)>c:
                right-=1
            else:
                left+=1
        return False