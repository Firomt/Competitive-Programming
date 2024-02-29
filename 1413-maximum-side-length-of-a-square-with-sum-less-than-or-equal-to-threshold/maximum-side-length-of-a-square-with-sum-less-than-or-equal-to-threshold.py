class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def squareSum(r1, c1, r2, c2):
            return preSum[r2][c2] - preSum[r1 - 1][c2] - preSum[r2][c1 - 1] + preSum[r1 - 1][c1 - 1]

        m, n = len(mat), len(mat[0])

        # preSum[i][j] := sum of all cells ending at mat[i][j] moving at right and down directions
        preSum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                curr = mat[i - 1][j - 1]
                diagonal = preSum[i - 1][j - 1]
                above = preSum[i - 1][j]
                left = preSum[i][j - 1]
                # preSum[i][j] = curr + diagonal + (above - diagonal) + (left - diagonal)
                #              = curr + above + left - diagonal
                preSum[i][j] = curr + above + left - diagonal

        res = 0

        # find square Sum starting at (i, j)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                limit = min(m - i, n - j)
                # build square with the size of l
                for l in range(limit + 1):
                    curr_sum = squareSum(i, j, i + l, j + l)

                    # valid; update the maximum side-length
                    if curr_sum <= threshold:
                        res = max(res, l + 1)

        return res