class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[0,1,1]
        next=0
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            for i in range(3,n+1):
                next=arr[i-3]+arr[i-2]+arr[i-1]
                arr.append(next)
        return arr[-1]