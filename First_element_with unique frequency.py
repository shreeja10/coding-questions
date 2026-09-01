class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new={}
        freq={}
        for i in nums:
            if i not in new:
                new[i]=1
            elif i in new:
                new[i]+=1
        for value in new.values():
            if value not in freq:
                freq[value]=1
            else:
                freq[value]+=1
        for i in nums:
            if freq[new[i]]==1:
                return i
        return -1