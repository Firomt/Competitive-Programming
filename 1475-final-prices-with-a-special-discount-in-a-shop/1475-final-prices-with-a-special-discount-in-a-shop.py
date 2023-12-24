class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        for i,p in enumerate(prices):
            while stack and p <= stack[-1][0]:
                price,ind=stack.pop()
                pay=price-p
                prices[ind]=pay
            stack.append([p,i])
        return prices
        