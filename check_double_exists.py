class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and 0 <= i and j < len(arr) and arr[i] == 2 * arr[j]:
                    return True

        return False
