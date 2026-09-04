class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        current=0
        pattern=""
        times=0
        times2=0
        for i in range(1,len(str2)+1):
            current=str2[:i]
            if len(str1)%len(current)==0:
                times=len(str1)//len(current)
                if current*times==str1:
                    if len(str2)%len(current)==0:
                        times2=len(str2)//len(current)
                        if current*times2==str2:
                            pattern=current
        return pattern