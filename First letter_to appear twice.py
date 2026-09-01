class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_set=set()
        for i in s:
            if i in s_set:
                return i
            s_set.add(i)
        return ""