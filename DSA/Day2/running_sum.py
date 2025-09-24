class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        l=[]
        for x in nums:
            sum+=x
            l.append(sum)
        return l
    
        #timecomplexity=O(n)    
        #spacecomplexity=O(1)
    
