class Solution(object):
    def countOppositeParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in range(len(nums)):
            count=0
            for j in range(i+1,len(nums)):
                if nums[i]%2==0 and nums[j]%2!=0:
                    count+=1
                elif nums[i]%2!=0 and nums[j]%2==0:
                    count+=1
            new.append(count)
        return new