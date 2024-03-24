class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        if len(flowerbed)==1:
            if flowerbed[0]==0 and n<=1:
                return True
            return False

        for i in range(len(flowerbed)-2):
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
                    if n==0:
                        return True
            elif i>0:
                if flowerbed[i]==0:
                    if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                        flowerbed[i]=1
                        n-=1
                        if n==0:
                            return True
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            n-=1

        return n==0
    
        