class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        d={}
        new=[]
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in arr:
            if d[i]==1:
                new.append(i)
        if k>len(new):
            return ""
        else:
            return(new[k-1])