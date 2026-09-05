class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new = set()
        i = 0
        j = 0
        k = 0
        number = 0
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and i != k and j != k and digits[i] != 0 and digits[k] % 2 == 0:
                        number = digits[i] * 100 + digits[j] * 10 + digits[k]
                        new.add(number)
        return sorted(new)
