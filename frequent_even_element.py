class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        ans=-1
        largest=0
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for keys,values in d.items():
            if keys%2==0:
                if values>largest:
                    largest=values
                    ans=keys
                elif values==largest:
                    ans=(min(ans,keys))
        return ans