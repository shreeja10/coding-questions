class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        total=0
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            while n>0:
                last=n%10
                total+=last**2
                n=n//10
            n=total
            total=0
        return True