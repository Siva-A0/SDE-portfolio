class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l=[[1],[1,1]]
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            i=3
            while i<=numRows:
                k=[]
                for j in range(i):
                    if j==0 or j==i-1:
                        k.append(1)
                    else:
                        v=l[i-2][j-1]+l[i-2][j]
                        k.append(v)
                i+=1
                l.append(k)
        return l
        
#time complexity O(n^2)
#space complexity O(1)