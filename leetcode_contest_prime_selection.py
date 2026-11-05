class Solution(object):
    def maxPrimes(self, n, s):
        """
        :type n: int
        :type s: int
        :rtype: List[int]
        """
        new=[]
        total=0
        for i in range(1,n+1):
            for j in range(2,n+1):
                if i%j!=0:
                    new.append(i)
        for i in range(len(new)):
            while total<=s:
                total+=new[i]
        return new

    def obj=Solution()
    print(obj.maxPrimes(7,20))