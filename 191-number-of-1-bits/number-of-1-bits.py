class Solution:
    def hammingWeight(self, n: int) -> int:
    
        binary_rep = bin(n)[2:]
        return binary_rep.count('1')
        