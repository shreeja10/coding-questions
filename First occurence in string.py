class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        current=0
        for i in range(len(haystack)-len(needle)+1):
            current=haystack[i:i+len(needle)]
            if current==needle:
                return i
        return -1