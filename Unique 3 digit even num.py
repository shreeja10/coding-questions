class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        i=0
        j=0
        k=0
        number=0
        new=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i!=j and i!=k and j!=k and digits[k]%2==0 and digits[i]!=0:
                        numbers=digits[i]*100+digits[j]*10+digits[k]
                        new.add(numbers)
        return len(new)