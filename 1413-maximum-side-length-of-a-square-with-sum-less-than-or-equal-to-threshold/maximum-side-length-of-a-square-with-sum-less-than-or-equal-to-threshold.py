class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows,cols=len(mat),len(mat[0])
        prefix_sum=[[0]*(cols+1) for _ in range(rows+1)]

        for i in range(rows):
            for j in range(cols):
                prefix_sum[i+1][j+1]=mat[i][j]+prefix_sum[i][j+1]+prefix_sum[i+1][j]-prefix_sum[i][j]

        def sumsquare(r1,c1,r2,c2):
            return prefix_sum[r2+1][c2+1]-prefix_sum[r2+1][c1]-prefix_sum[r1][c2+1]+prefix_sum[r1][c1]
        

        best=0
        for i in range(rows):
            for j in range(cols):
                for k in range(best, min(rows-i,cols-j)):
                    if sumsquare(i,j,i+k,j+k) <= threshold:
                        best=k+1
                    else: 
                        break

        return best