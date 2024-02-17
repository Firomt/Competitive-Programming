class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        nxt_pile=len(piles)-2
        n=len(piles)/3
        total=0
        while n>0:
            total+=piles[nxt_pile]
            nxt_pile-=2
            n-=1
        return total
        