class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d1={}
        d2={}
        for i in s:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for i in t:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1
        for keys,values in d2.items():
            if keys not in d1 or values > d1[keys]:
                return keys