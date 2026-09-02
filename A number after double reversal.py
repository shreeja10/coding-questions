class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        last=0
        rev=0
        original=num

        while num>0:
            last=num%10
            rev=rev*10+last
            num=num//10
        end=0
        rev_rev=0
        while rev>0:
            end=rev%10
            rev_rev=rev_rev*10+end
            rev=rev//10
        if rev_rev==original:
            return True
        else:
            return False