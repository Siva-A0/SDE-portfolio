class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        v=1
        z=0

        for x in nums:
            if x!=0:
                v*=x
            else:
                z+=1
            
        if z>=1:
            if z==1:
                for i in range(len(nums)):
                    if nums[i]!=0:
                        nums[i]=0
                    else:
                        nums[i]=v
            else:
                nums=[0 for x in nums]

        else:
            for i in range(len(nums)):
                nums[i]=v//nums[i]

        print(nums)
        return nums

# time complexity: O(n)
# space complexity: O(1)