class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        new=[]
        min_sum=float('inf')
        ans=[]
        index_sum=0
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    index_sum=i+j
                    if index_sum<min_sum:
                        min_sum=index_sum
                        ans=[list1[i]]
                    elif index_sum==min_sum:
                        ans.append(list1[i])
        return ans