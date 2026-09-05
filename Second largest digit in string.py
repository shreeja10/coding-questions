class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        new = []
        for i in s:
            if i.isnumeric():
                new.append(int(i))
        if not new:
            return -1
        largest = new[0]
        second_largest = float('-inf')
        for i in new:
            if i > largest:
                largest = i
        for i in new:
            if i != largest and i > second_largest:
                second_largest = i
        if second_largest == float('-inf'):
            return -1
        return second_largest
