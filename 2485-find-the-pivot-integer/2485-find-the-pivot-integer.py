class Solution:
    def pivotInteger(self, n: int) -> int:
        total=0
        leftsum=0
        for i in range(n+1):
            total+=i
        for i in range(n+1):
            leftsum+=i
            rightsum=total-leftsum+i
            if leftsum==rightsum:
                return i
        return -1
            
            