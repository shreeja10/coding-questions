class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = ""
        n = ""
        for i in range(len(s)):
            if s[i] == "#":
                m = m[:-1]
            else:
                m += s[i]
        for i in range(len(t)):
            if t[i] == "#":
                n = n[:-1]
            else:
                n += t[i]
        return m == n
