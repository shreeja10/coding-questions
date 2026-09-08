class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num%3!=0:
            return []
        i=num//3
        return[i-1,i,i+1]