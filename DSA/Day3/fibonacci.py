class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            fib0=0
            fib1=1
            for _ in range(n-1):
                fib0,fib1=fib1,fib0+fib1
            
        return fib1
        
    #Time complexity: O(n)
    #Space complexity: O(1)