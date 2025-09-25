class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        for x in range(1,len(nums)):
            if nums[i]!=nums[x]:
                i+=1
                nums[i],nums[x]=nums[x],nums[i]
        return i+1
            
#time complexity O(n)
#space complexity O(1)