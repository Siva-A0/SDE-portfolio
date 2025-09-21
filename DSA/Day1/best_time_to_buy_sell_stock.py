class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        minny=99999
        for x in prices:
            if minny > x:
                minny = x
            if (x-minny) > max_profit:
                max_profit  = x-minny
        return max_profit
    
# Time Complexity: O(n)
# Space Complexity: O(1)
