class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=0
        right=len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                s1=s[:left]+s[left+1:]
                s2=s[:right]+s[right+1:]
                if s1[::-1]==s1 or s2[::-1]==s2:
                    return True
                else:
                    return False
        return True
