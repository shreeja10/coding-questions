class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word=""
        new=[]
        left=0
        for i in range(len(s)):
            if s[i]==" ":
                word=s[left:i]
                word=word[::-1]
                new.append(word)
                new.append(" ")
                left=i+1
        for i in s[-1]:
            word = s[left:]
            word = word[::-1]
            new.append(word)
        return("".join(new))