class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for x in range(len(nums)):
            ele=target-nums[x]
            if ele in dic:
                return [dic[ele],x]
            else:
                dic[nums[x]]=x

# Time Complexity: O(n)
# Space Complexity: O(n)
        