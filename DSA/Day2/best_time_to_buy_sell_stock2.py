class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        profit=0
        maxy=99999
        for x in prices:
            if maxy>x:
                maxy=x
            if x-maxy>profit:
                profit=x-maxy
            elif x-maxy<profit:
                max_profit+=profit
                maxy=x
                profit=0
                
        return(max_profit+profit)
        
        #timecomplexity=O(n)
        #spacecomplexity=O(1)