class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in nums1:
            if (i in nums2 or i in nums3) and i not in new:
                new.append(i)
        for j in nums2:
            if (j in nums1 or j in nums3) and j not in new:
                new.append(j)
        for k in nums3:
            if (k in nums1 or k in nums2) and k not in new:
                new.append(k)
        return new
