class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_digits = 0

        for i in nums:

            count = 0
            n = i

            while n > 0:
                last = n % 10
                count += 1
                n = n // 10

            if count % 2 == 0:
                even_digits += 1

        return even_digits