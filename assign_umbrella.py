class Solution(object):
    def assignUmbrella(self, rain):
        """
        :type rain: List[int]
        :rtype: List[str]
        """
        a=0
        b=0
        new=[]
        for i in range(len(rain)-1):
            if rain[i]==1 and rain[i+1]==1:
                if a==b:
                    new.append("Alice")
                    a+=1
                elif a>b:
                    new.append("Bob")
                    b+=1
                elif a<b:
                    new.append("Alice")
                    a+=1
            elif rain[i]==1 and rain[i+1]==0:
                new.append("Bob")
                b+=1
            elif rain[i]==0:
                new.append("None")
        if rain[-1]==1:
            new.append("Bob")
            b+=1
        else:
            new.append("None")
        return new  ©leetcode