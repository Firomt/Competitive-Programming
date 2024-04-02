class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        basket = {}
        total = 0
        l =0
        for r in range(len(fruits)):
            basket[fruits[r]] = 1 + basket.get(fruits[r], 0)
            total += 1

            while len(basket) > 2:
                f = fruits[l]
                basket[f] -= 1
                total -= 1
                l += 1
                if basket[f]==0:
                    basket.pop(f)
            res = max(res, total)
        return res
            
                
        