class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        volume=length*width*height
        if (length>=10**4 or width>=10**4 or height>=10**4 or volume>=10**9) and mass>=100:
            return("Both")
        elif length>=10**4 or width>=10**4 or height>=10**4 or volume>=10**9:
            return ("Bulky")
        elif mass>=100:
            return("Heavy")
        elif length<10**4 or width<10**4 or height<10**4 or volume<10**9 and mass<100:
            return("Neither")
        elif length>=10**4 or width>=10**4 or height>=10**4 or volume>=10**9 and mass<100:
            return("Bulky")
        elif length<10**4 and width<10**4 and height<10**4 and volume<10**9 and mass>=100:
            return("Heavy")