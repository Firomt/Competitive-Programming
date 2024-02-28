class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols=len(matrix),len(matrix[0])
        self.prefixsum=[[0]*(cols+1) for c in range(rows+1)]
        for r in range(rows):
            prefix=0
            for c  in range (cols):
                prefix+=matrix[r][c]
                above_sum=self.prefixsum[r][c+1]
                self.prefixsum[r+1][c+1]=prefix+above_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,r2,c1,c2=row1+1,row2+1,col1+1,col2+1
        topsum=self.prefixsum[r1-1][c2]
        bottomright=self.prefixsum[r2][c2]
        leftsum=self.prefixsum[r2][c1-1]
        topleft=self.prefixsum[r1-1][c1-1]
        return bottomright-topsum-leftsum+topleft

    
    
    
    
        #topleftsum is subtracted twice so it is added once to offset it

        #abovesum= the  prefix sum of the area just above the given portion array
        #leftsum = the  prefix sum of the area to the left of the given portion of the array
        
       

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)