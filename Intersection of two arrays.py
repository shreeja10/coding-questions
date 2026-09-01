class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set=set(nums1)
        nums2_set=set(nums2)
        nums3=[]
        for i in nums1_set:
            if i in nums2_set:
                nums3.append(i)
        return nums3