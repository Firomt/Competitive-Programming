class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        largest_bit, cnt = 0, 0
        for i, bit in enumerate(flips, 1):
            largest_bit = max(largest_bit, bit)
            if largest_bit == i:
                cnt += 1
        return cnt
        