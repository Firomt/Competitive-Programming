class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r, max_frt = 0, 0, 0
        basket = {}
        while r < len(fruits):
            if len(basket) < 2 or fruits[r] in basket:
                basket[fruits[r]] = 1 + basket.get(fruits[r], 0)
            else:
                max_frt = max(max_frt, r - l)
                while len(basket) >= 2:
                    removed = fruits[l]
                    basket[removed] -= 1
                    if basket[removed] == 0:
                        del basket[removed]
                    l += 1
                basket[fruits[r]] = 1
            r += 1
            
        return max(max_frt, r-l)
        

