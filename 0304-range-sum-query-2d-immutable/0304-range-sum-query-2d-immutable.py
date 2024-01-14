class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols=len(matrix),len(matrix[0])
        self.prefixsum_mat=[[0]*(cols+1) for r in range(rows + 1)]
        for  r in range(rows):
            prefix=0
            for c in range(cols):
                prefix += matrix[r][c]
                above=self.prefixsum_mat[r][c+1]
                self.prefixsum_mat[r+1][c+1]=prefix + above
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRightsum=self.prefixsum_mat[row2+1][col2+1]
        abovesum=self.prefixsum_mat[row1][col2+1]
        leftsum=self.prefixsum_mat[row2+1][col1]
        topleftsum=self.prefixsum_mat[row1][col1]
        return bottomRightsum - leftsum - abovesum + topleftsum 
        #topleftsum is subtracted twice so it is added once to offset it

        #abovesum= the  prefix sum of the area just above the given portion array
        #leftsum = the  prefix sum of the area to the left of the given portion of the array
        
       

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)