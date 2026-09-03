class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict_note={}
        dict_mag={}
        for i in ransomNote:
            if i not in dict_note:
                dict_note[i]=1
            else:
                dict_note[i]+=1
        for i in magazine:
            if i not in dict_mag:
                dict_mag[i]=1
            else:
                dict_mag[i]+=1
        for i in ransomNote:
            if i not in magazine or dict_note[i]>dict_mag[i]:
                return False
        return True