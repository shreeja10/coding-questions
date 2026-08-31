class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        result_s=sorted(s)
        result_t=sorted(t)
        if result_s==result_t:
            return True
        else:
            return False