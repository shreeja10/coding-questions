class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        new = []
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                new = [left + 1, right + 1]
                return new
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
