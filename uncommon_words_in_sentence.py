class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        new=[]
        s1=(s1.split())
        s2=(s2.split())
        count={}
        c={}
        for i in s1:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for i in s2:
            if i not in c:
                c[i]=1
            else:
                c[i]+=1
        for i in s1:
            if i not in s2 and count[i]==1:
                new.append(i)
        for i in s2:
            if i not in s1 and c[i]==1:
                new.append(i)
        return new