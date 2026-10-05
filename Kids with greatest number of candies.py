class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        largest=0
        for i in range(len(candies)):
            if candies[i]>largest:
                largest=candies[i]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=largest:
                result.append(True)
            else:
                result.append(False)
        return result