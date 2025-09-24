class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        t=sum(nums)
        for x in range(len(nums)):
            if l==t-l-nums[x]:
                return x
            else:
                l+=nums[x]
        return -1
        

    #Timecomplexity: O(n)
    #Spacecomplexity: O(1)         