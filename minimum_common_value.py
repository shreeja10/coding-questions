class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i,j=0,0
        new=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                new.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        if len(new)==0:
            return -1
        else:
            return min(new)