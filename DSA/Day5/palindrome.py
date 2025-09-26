class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return str(x)==str(x)[::-1]

        n=x
        v=0
        if x<0: return False
        while n:
            v=v*10+n%10
            n//=10
        return x==v
        
# time complexity: O(n) 
# space complexity: O(1)