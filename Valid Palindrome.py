class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()

        new = ""

        for i in s:
            if i.isalnum():
                new += i
        if new==new[::-1]:
            return True
        else:
            return False