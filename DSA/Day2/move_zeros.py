class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos=0
        for x in range(len(nums)):
            if nums[x]!=0:
                nums[x],nums[pos]=nums[pos],nums[x]
                pos+=1
        return nums