class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        cost = []

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):

                if prices[i] + prices[j] <= money:
                    cost.append(prices[i] + prices[j])

        if cost:
            return money - min(cost)
        else:
            return money