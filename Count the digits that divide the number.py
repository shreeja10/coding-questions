class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        last=0
        count=0
        original=num
        while num>0:
            last=num%10
            if original%last==0:
                count+=1
            num=num//10
        return count