class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        c1 = {}
        c2 = {}
        new = 0
        for i in words1:
            if i not in c1:
                c1[i] = 1
            else:
                c1[i] += 1
        for i in words2:
            if i not in c2:
                c2[i] = 1
            else:
                c2[i] += 1
        for i in words1:
            if i in words2 and c1[i] == 1 and c2[i] == 1:
                new += 1
        return new
