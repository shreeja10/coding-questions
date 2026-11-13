class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d={}
        new=[]
        a={}
        for i in range(len(arr)):
            d[arr[i]]=d.get(arr[i],0)+1
        for keys,values in d.items():
            new.append(values)
        for i in range(len(new)):
            a[new[i]]=a.get(new[i],0)+1
        for keys,values in a.items():
            if values!=1:
                return False
        return True