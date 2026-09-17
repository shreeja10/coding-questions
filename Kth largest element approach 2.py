class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for j in range(k):
            largest=float('-inf')
            for i in nums:
                if i>largest:
                    largest=i
            nums.remove(largest)
        return largest