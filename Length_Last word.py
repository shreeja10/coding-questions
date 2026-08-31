class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split()
        a=s[-1]
        count=0
        for letter in a:
            count+=1
        return count