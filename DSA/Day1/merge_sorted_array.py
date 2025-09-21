class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        num=nums1[:m]
        i=j=k=0

        while i<m and j<n:
            if num[i]<=nums2[j]:
                nums1[k]=num[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            k+=1
        
        while i<m:
            nums1[k]=num[i]
            i+=1
            k+=1
        
        while j<n:
            nums1[k]=nums2[j]
            j+=1
            k+=1
        
        return nums1

# Time Complexity: O(m+n)
# Space Complexity: O(1)