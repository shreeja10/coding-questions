class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=s.split()
        result=result[::-1]
        result=" ".join(result)
        return result