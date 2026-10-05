class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product=1
        total=0
        result=0
        last=0
        while n>0:
            last=n%10
            product*=last
            total+=last
            n=n//10
        result=product-total
        return result