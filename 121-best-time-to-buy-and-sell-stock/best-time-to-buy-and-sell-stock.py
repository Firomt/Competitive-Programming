class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j=0,1
        best=0

        while j < len(prices):
            if prices[i]<prices[j]:
                cur_best=prices[j]-prices[i]
                best=max(best,cur_best)
            else:
                i=j
            j+=1

        return best


        
        
        