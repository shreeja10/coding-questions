class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d1={}
        d2={}
        w=s.split()
        if len(w)!=len(pattern):
            return False
        for i in range(len(w)):
            if w[i] not in d1:
                d1[w[i]]=pattern[i]
            else:
                if d1[w[i]]!=pattern[i]:
                    return False
        for i in range(len(pattern)):
            if pattern[i] not in d2:
                d2[pattern[i]]=w[i]
            else:
                if d2[pattern[i]]!=w[i]:
                    return False
        return True