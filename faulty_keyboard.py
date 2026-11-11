class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        new=""
        for i in range(len(s)):
            if s[i]=="i":
                new=new[::-1]
            else:
                new+=s[i]
        return new