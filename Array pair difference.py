class Solution(object):
    def check(self, nums, k):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if abs(nums[i] - nums[j]) == k:
                    return True

        return False
