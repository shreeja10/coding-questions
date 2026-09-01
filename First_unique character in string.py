class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        new={}
        for i in s:
            if i not in new:
                new[i]=1
            else:
                new[i]+=1
        for i in range(len(s)):
            if new[s[i]]==1:
                return i
        return -1