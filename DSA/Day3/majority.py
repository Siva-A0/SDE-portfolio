class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # return nums[(len(nums)//2)]

        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for x in d:
            if d[x]>len(nums)//2:
                return x
            
    #time complexity: O(n)
    #space complexity: O(n)